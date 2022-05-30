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


conn = sqlite3.connect('db.sqlite3')
curs = conn.cursor()


def get_song_data(song_title='song_title'):
    """Function to query DB for user-input song, pull values into an array and run through ML model"""
    # Get song name from user request
    song_title = request.values['song_title']
    
    # Query DB for user-submitted song title
    
    
    # Convert song title into 2D array of song data
    
    return



###### SCRATCH ##########


# # Get our API keys
# key = getenv('SPOTIFY_API_KEY')
# secret = getenv('SPOTIFY_API_KEY_SECRET')

# # Authenticate with spotipy
# client_credentials_manager = SpotifyClientCredentials(client_id = key,
#                                                      client_scret = secret)
# sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


def get_song_data(song_title='song_title'):
    """Function to query DB for user-input song, pull values into an array and run through ML model"""
    
    # Get song name from user request
    song_title = request.values['song_title']
    # print(type(song_title)) - str
    
    # Query DB for user-submitted song title
    song_data = song.query.filter(song.name == f'{song_title}')
    
    
    # params = song_title
    # USE_COLUMNS = '''SELECT (explicit, danceability, energy, 
    #                                 "key", loudness, mode, speechiness, 
    #                                 acousticness, time_signature, year)
    #                                 FROM song
    #                                 WHERE name = ?;'''
    # USE_COLUMNS = '''SELECT * FROM song WHERE name = ?'''
    # song_data = song.query.all(usable_columns)
    # song_data = curs.execute(USE_COLUMNS, song_title).fetchone()
    
    print('song_data', type(song_data))
    
    ##### change str back to list
#     track_list = [[(item) for item in [song_data]]]
#     print(track_list)
    
    # track_list_str = []
    

    
    # Convert song title into 2D array of song data
    user_song = [list(song_data)]
    print('user_song', type(user_song))
    print(user_song)
  

    
    song_data_array = np.array(user_song).reshape(1,-1).astype(float)
    # song_data_array = pd.astype(float)
    # print(type(song_data_array)) - numpy array
    # print(song_data_array.shape) - (1,1)
    print(song_data_array)
    
    # for i in song_data_array[0][0:9]:
    #     song_data_array[i].astype(str)#.astype(float)
    # print('song_data_array', song_data_array[0], type(song_data_array[0][0]))
    
    
    
    # # Load Nearest Neighbors model
    loaded_model = load('model.sav')
    distances, song_indexes = loaded_model.kneighbors(song_data_array, 6)
    
    # # load pickle model
    # loaded_pickle = pickle.load(open('pickle_model.sav'), 'rb')
    # distances, song_indexes = loaded_pickle.kneighbors(usa, 6)
    
    # usa = [[False,  0.499, 0.899, 4, -8.478, 1, 0.2769999999999999, 2.13e-05, 4.0, 2006]]
    # print(usa)
    # print('usa', type(usa))
    # loaded_model = load('model.sav')
    # distances, song_indexes = loaded_model.kneighbors(usa, 6)
    print(type(song_indexes))

    return song_indexes
    
    # Consider multiple songs with same name...
    
    
    
    
#### WITH HENRY's HELP ######

    def get_song_data(song_title='song_title'):
    """Function to query DB for user-input song, pull values into an array and run through ML model"""
    
    # Get song name from user request
    song_title = request.values['song_title']
    
    # Query DB for user-submitted song title
    song_data = song.query.filter(song.name == f'{song_title}')
    print('song_data', type(song_data)) # query
    
    # Convert song title into 2D array of song data
    
    user_song = list(song_data)
    print("type of user song", type(user_song), type(user_song[0]), user_song[0])
    newThing = np.array(user_song[0])
    
    print(type(newThing))
    print(newThing)
    newThing.astype(str)
    print("should be a string", newThing)
    # print(type(user_song), user_song)

#     pd.to_numeric(user_song)
#     print('user_song', type(user_song))
#     print(user_song)
      

    
    # song_data_array = np.array(user_song).reshape(1,-1) 
    # song_data_array.astype(float)
    # for i in song_data_array:
    #     i.astype(float)#.astype(float)
    # print('song_data_array', song_data_array[0], type(song_data_array[0][0]))
    
    # # Load Nearest Neighbors model
    loaded_model = load('model.sav')
    # print(type(song_data_array))
    _, song_indexes = loaded_model.kneighbors(newThing, 6)
    

    print(type(song_indexes))

    return song_indexes
    
    # Consider multiple songs with same name...
    