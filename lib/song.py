class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes through class methods
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        # Only add genre if it's not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        # Only add artist if it's not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        # Update genre count histogram
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        # Update artist count histogram
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1