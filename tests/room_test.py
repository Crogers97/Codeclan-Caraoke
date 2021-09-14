import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Fleetwood Mac", "The Chain")
        self.song_2 = Song("Queen", "Dont stop me now")
        self.song_3 = Song("Michael Jackson", "Thriller")
        self.song_4 = Song("Bob Marley", "Buffalo Soldier")
        self.guest_1 = Guest("Calum", 40, "The Chain")
        self.guest_2 = Guest("Will", 10,"Dont stop me now")
        self.guest_3 = Guest("Tony", 25, "Thriller")
        self.guest_4 = Guest("Lewis", 50, "Welcome to the jungle")
        self.room_1 = Room("Rock",5)
        self.room_2 = Room("Pop", 2)
        self.room_3 = Room("Rap", 7)
    @unittest.skip("Delete this line to run the test")
    def test_check_in_guest(self):
        guest = self.guest_1
        self.room_1.check_in(guest)
        self.assertEqual(1, self.room_1.room_count())   
    @unittest.skip("Delete this line to run the test")
    def test_check_out_guest(self):
        guest = self.guest_1
        self.room_2.check_in(guest)
        self.room_2.check_out(guest)
        self.assertEqual(0, self.room_2.room_count()) 
    @unittest.skip("Delete this line to run the test")
    def test_add_songs_to_room(self):
        song = self.song_1
        self.room_1.add_song(song)
        self.assertEqual(1, self.room_1.song_count())
    @unittest.skip("Delete this line to run the test")
    def test_more_than_capacity(self):
        guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]
        self.room_2.entry_denied(guests)
        self.assertEqual(0, self.room_2.room_count())
    
    def test_guest_favourite_song_is_in_the_room(self):
        self.room_2.check_in(self.guest_1)
        self.room_2.add_song(self.song_1)
        self.assertEqual("whoo!", self.room_2.check_favourite_song(self.guest_1))

    def test_guest_favourite_song_is_not_in_the_room(self):
        self.room_2.check_in(self.guest_1)
        self.room_2.add_song(self.song_4)
        self.assertEqual("booo", self.room_2.check_favourite_song(self.guest_1))
    



