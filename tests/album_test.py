import unittest
from models.album import Album
from models.artist import Artist


class TestAlbum(unittest.TestCase):
    def setUp(self) :
        self.artist_1 = Artist ('Dave',30)
        self.artist_1.id = 1
        self.album_1 = Album('Dave The Album',10, self.artist_1)
        # self.album_2 = Album('The Sequel of Dave',15, self.artist_1.artist_id)
        # self.album_3 = Album('Dave no more',5, self.artist_1.artist_id)

    def test_album_name(self):
        self.assertEqual('Dave The Album', self.album_1.name)

    def test_songs(self):
        self.assertEqual(10, self.album_1.songs)

    def test_artist_id(self):
        artist_2 = Artist('Rick', 28)
        artist_2.id = 2
        album_2 =Album('The Sequel of Dave',15,artist_2)
        self.assertEqual(1, self.album_1.artist.id)
        self.assertEqual(2, album_2.artist.id)

