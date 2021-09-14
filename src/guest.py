from src.venue import Venue

class Guest:

    def __init__(self, name, money, favourite_song):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song
    
    def sufficient_funds(self, entry:Venue):
        return self.money >= entry.fee

