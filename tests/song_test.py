from src.song import Song
import unittest


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Yesterday", "The Beatles")

    def test_song_has_title_and_artist(self):
        self.assertEqual("Yesterday", self.song.title)
        self.assertEqual("The Beatles", self.song.artist)
