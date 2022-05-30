# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import getenv
import sqlite3
import pandas as pd
import numpy as np
from joblib import dump, load
from sklearn.neighbors import NearestNeighbors
from .models import song
from flask import request
import pickle


def get_song_data(song_title='song_title'):
    """Function to query DB for user-input song, pull values into an array and run through ML model"""
    
    # Get song name from user request
    song_title = request.values['song_title']
    
    # Query DB for user-submitted song title
    song_data = song.query.filter(song.name == f'{song_title}')
    print('song_data', type(song_data)) # query
    
    # Convert song title into 2D array of song data
    user_song = [list(item) for item in [song_data]]
    print(type(user_song), user_song)
    
    song_data_array = np.array(user_song).reshape(1,-1) 
    # song_data_array.astype(float)
    # for i in song_data_array:
    #     i.astype(float)#.astype(float)
    print('song_data_array', song_data_array[0][0], type(song_data_array))
    
    # # Load Nearest Neighbors model
    loaded_model = load('model.sav')
    # print(type(song_data_array))
    _, song_indexes = loaded_model.kneighbors(song_data_array, 6)
    

    print(type(song_indexes))

    return song_indexes
    
    # Consider multiple songs with same name...
    
    
    
    
# def another_fxn():
   
#    """get row ids of recommended songs, query for those songs names, and
#     return recommendations"""
#     # Run song data through ML model

    
#     # Retrieve song row ids
    
#     # Query for song titles by row ids
    
#     # Return recommended song titles and artist to user
#     pass

    
    
    
    
# Load dataset and sample it down to 8% of the original size
# Reset index after sampling to make indices easier to reason about
df = pd.read_csv('tracks_features.csv')
# df = df.sample(frac=.08, random_state=42).reset_index()

# Drop old index to avoid confusing it for the new one
# df = df.drop(columns=['index'])

# Check for null values
# df.isnull().sum()


# Convert True/False in explicit column to 1s and 0s
df['explicit'] = df['explicit'].astype(int)

# Create X Matrix of numeric song attributes
usable_columns =['explicit', 'danceability', 'energy', 'key', 'loudness', 
        'mode', 'speechiness', 'acousticness', 'time_signature', 'year',
                'tempo', 'liveness', 'valence', 'instrumentalness']
X = df[usable_columns]

# Use NearestNeighbors to get 5 most similar songs
neigh = NearestNeighbors(n_neighbors=5, n_jobs=-1)
neigh.fit(X)


if __name__ == '__main__':
    print(df.head())
    print(df.isnull().sum().sum())