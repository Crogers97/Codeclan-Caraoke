import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Fleetwood Mac", "Dreams")
    @unittest.skip("Delete this line to run the test")
    def test_song_has_artist(self):
        self.assertEquals("Fleetwood Mac", self.song.artist)
    @unittest.skip("Delete this line to run the test")
    def test_song_has_title(self):
        self.assertEquals("Dreams", self.song.title)
