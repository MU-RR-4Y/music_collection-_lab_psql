import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):
    def setUp(self) :
        self.artist_1 = Artist('Dave', 30)
        self.artist_2 = Artist('Rick', 28)

    def test_artist_name(self):
        self.assertEqual('Dave', self.artist_1.name)

    def test_age(self):
        self.assertEqual(28,self.artist_2.age)

    def test_id(self):
        self.artist_2.id = 1
        self.assertIsNone(self.artist_1.id)
        self.assertEqual(1, self.artist_2.id)
