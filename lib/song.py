class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


if __name__ == "__main__":
    from song import Song

    Song.count = 0
    Song.genre_count = {}
    Song.artist_count = {}

    class TestSong:
        '''Class "Song" in song.py'''

        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")

        def test_saves_name_artist_genre(self):
            '''instantiates with a name, artist, and genre.'''
            out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
            assert(out_of_touch.name == "Out of Touch")
            assert(out_of_touch.artist == "Hall and Oates")
            assert(out_of_touch.genre == "Pop")

        def test_has_song_count(self):
            '''counts the total number of Song objects.'''
            assert(Song.count == 4)
            Song("Sara Smile", "Hall and Oates", "Pop")
            assert(Song.count == 5)

        def test_has_genres(self):
            '''keeps track of all Song genres.'''
            assert("Rap" in Song.genres)
            assert("Pop" in Song.genres)
            assert("Rock" in Song.genres)

        def test_has_artists(self):
            '''keeps track of all Song artists.'''
            assert("Jay Z" in Song.artists)
            assert("Beyonce" in Song.artists)
            assert("Hall and Oates" in Song.artists)
            
        def test_has_genre_count(self):
            '''keeps count of Songs for each genre.'''
            assert(Song.genre_count["Rap"] == 1)
            assert(Song.genre_count["Pop"] == 3)
            assert(Song.genre_count["Rock"] == 1)

        def test_has_artist_count(self):
            '''keeps count of Songs for each artist.'''
            assert(Song.artist_count["Jay Z"] == 1)
            assert(Song.artist_count["Beyonce"] == 1)
            assert(Song.artist_count["Nirvana"] == 1)
            assert(Song.artist_count["Hall and Oates"] == 2)
    
    