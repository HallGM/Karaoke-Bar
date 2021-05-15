class Room:
    def __init__(self, capacity, entry_fee):
        self._songs = []
        self._guests = []
        self.capacity = capacity
        self.entry_fee = entry_fee

    def add_song(self, song):
        self._songs.append(song)

    def check_in(self, guest):
        # Check Capacity
        if len(self._guests) >= self.capacity:
            return
        # Take Payment
        if not guest.pay_entry_fee(self):
            return
        # Add guest to room
        self._guests.append(guest)
        # Check if their favorite song is in the room
        song_titles = [song.title for song in self._songs]
        if guest.favourite_song in song_titles:
            return "Whoo!"

    def check_out(self, guest):
        self._guests.remove(guest)
