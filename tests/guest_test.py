import unittest
from src.guest import Guest
from src.venue import Venue
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Calum", 20, "Living on a prayer")
        self.guest_2 = Guest('Will', 3, "Dancing Queen")
        self.venue = Venue("CodeClan Caraoke", 5 )
    @unittest.skip("Delete this line to run the test") 
    def test_guest_has_name(self):
        self.assertEquals("Calum", self.guest.name)
    @unittest.skip("Delete this line to run the test")
    def test_guest_has_money(self):
        self.assertEquals(20, self.guest.money)
    
    def test_guest_has_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.venue))
    
    def test_sufficient_funds__false_if_not_enough(self):
        self.assertEqual(False, self.guest_2.sufficient_funds(self.venue))

    def test_guest_has_a_favourite_song(self):
        self.assertEqual("Dancing Queen", self.guest_2.favourite_song)
    
    # def test_guest_can_enter__decrease_money(self):
    #     self.assertEqual()

    
    
    






