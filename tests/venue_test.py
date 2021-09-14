import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.venue import Venue


class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke", 5 )

    def test_venue_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)
    
    def test_has_venue_have_entry_fee(self):
        self.assertEqual(5, self.venue.fee)
    

    
    
