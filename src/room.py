class Room:

    def __init__(self, name, capacity):
        self.songs = []
        self.guests = []
        self.name = name
        self.capacity = capacity
       
    
    def room_count(self):
        return len(self.guests)

    def check_in(self, guest_to_check_in):
        self.guests.append(guest_to_check_in)
    
    def check_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)
    
    def song_count(self):
        return len(self.songs)
    
    def add_song(self, song_to_be_added):
        self.songs.append(song_to_be_added)
    
    def entry_denied(self, guests_wanting_entry):
        if len(guests_wanting_entry) > self.capacity:
            return 
        else:
            self.check_in
        return self.room_count

    def check_favourite_song(self, guest):
        for song in self.songs:
            if song.title == guest.favourite_song:
                return "whoo!"
        return "booo"
