import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Imagine", "John Lennon")
        self.song_2 = Song("Song 2", "Blur")
        self.guest_1 = Guest("Dave", 10, "Imagine")
        self.guest_2 = Guest("Sally", 20, "Song 2")
        self.guest_3 = Guest("Max", 10, "Barbie Girl")
        self.guest_4 = Guest("Adam", 30, "Highway to Hell")
        self.guest_5 = Guest("Alan", 50, "Hallelujah")
        self.guest_6 = Guest("Sue", 100, "Back in Black")
        self.poor_guest = Guest("Peter", 0, "Blue Christmas")
        self.guests = [
            self.guest_1,
            self.guest_2,
            self.guest_3,
            self.guest_4,
            self.guest_5,
            self.guest_6,
        ]
        self.room = Room(5, 10)

    def test_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual([self.song_1], self.room._songs)

    def test_check_in(self):
        self.room.check_in(self.guest_1)
        self.assertEqual([self.guest_1], self.room._guests)

    def test_check_out(self):
        self.room.check_in(self.guest_1)
        self.room.check_in(self.guest_2)
        self.room.check_out(self.guest_1)
        self.assertEqual([self.guest_2], self.room._guests)

    def test_room_doesnt_exceed_capacity(self):
        for guest in self.guests:
            self.room.check_in(guest)
        self.assertEqual(5, len(self.room._guests))

    def test_whoo_on_favourite_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual("Whoo!", self.room.check_in(self.guest_1))

    def test_no_money_no_entry(self):
        self.room.check_in(self.poor_guest)
        self.assertEqual(False, self.poor_guest in self.room._guests)
