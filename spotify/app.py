import pandas as pd
import sqlite3
from flask import Flask, render_template, request
from .models import DB, song
from .recommendation import get_song_data
from joblib import load
from os import getenv
from sklearn.neighbors import NearestNeighbors
from sqlalchemy import create_engine



def create_app():

    # Initialize our app
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)
    
    # Create routes for different pages
    @app.route("/")
    def home():
        return render_template('base.html', message='Spotify Recommender')

    
    @app.route("/populate")
    def populate():
        DB.drop_all()
        DB.create_all()
        df = pd.read_csv('tracks_features.csv')
        df = df.sample(frac=.08, random_state=42).reset_index()
        df = df.drop(columns=['index', 'disc_number', 'track_number', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'release_date'])
        df['explicit'] = df['explicit'].astype(int)
        
        sql_engine = create_engine('sqlite:///spotify/db.sqlite3', echo=False)
        df.to_sql('song', sql_engine, index=True, if_exists='replace')
        return "A database has been populated with songs from Spotify"
    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        # TODO: insert songs into DB
        return "Reset worked"

        
    @app.route('/recommend', methods=['POST'])
    def recommend():
        
        # TODO need try/except for exact match of spelling, punctuation and capitalization
        # Pull text from user input
        song_title = request.values['song_title']
        
        print(get_song_data())

                # usable_columns =['explicit', 'danceability', 'energy', 'key', 'loudness', 
                # 'mode', 'speechiness', 'acousticness', 'time_signature', 
                #  'year', 'tempo', 'liveness', 'valence', 'instrumentalness']

        # X = df[usable_columns]
        # Fake Recommended Song Data
        # TODO: Replace this with song recommendations from the ML model
        fake_recommendations = [['Ma Mélodie', 'Feet Peals'],
                                ['Minha Bênção (Ao Vivo)', 'Padre Marcelo Rossi'],
                                ['Stuck In A Glass Elevator', 'The Myriad'],
                                ['Club Hip Hop Beat 2', 'Jorge Quintero'],
                                ['Like...monk-like', 'The Reese Project']]

        return render_template('base.html',
                               message='Spotify Recommender',
                               songs=fake_recommendations)
        

    return app