from flask_sqlalchemy import SQLAlchemy

# creating the database and connecting to it
DB = SQLAlchemy()

class song(DB.Model):
    """Creates Song table"""
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # song title column
    name = DB.Column(DB.String, nullable=False)
    # album column
    album = DB.Column(DB.String)
    # album id column
    album_id = DB.Column(DB.String)
    # artist column
    artists = DB.Column(DB.String)
    # artist id column
    artist_ids = DB.Column(DB.String)
    # explicit column
    explicit = DB.Column(DB.Integer)
    # danceability column
    danceability = DB.Column(DB.Float)
    # energy column
    energy = DB.Column(DB.Float)
    # key column
    key = DB.Column(DB.Integer)
    # loudness column
    loudness = DB.Column(DB.Float)
    # mode column
    mode = DB.Column(DB.Integer)
    # speechiness column
    speechiness = DB.Column(DB.Float)
    # acousticness column
    acousticness = DB.Column(DB.Float)
    # time_signature column
    time_signature = DB.Column(DB.Float)
    # year column
    year = DB.Column(DB.Integer)


    def __iter__(self):
        # return {self.explicit},  {self.danceability}, {self.energy}, {self.key}, {self.loudness}, {self.mode}, {self.speechiness}, {self.acousticness}, {self.time_signature}, {self.year}
        return self.explicit,  self.danceability, self.energy, self.key, self.loudness, self.mode, self.speechiness, self.acousticness, self.time_signature, self.year
if __name__ == '__main__':
    print(type(DB))