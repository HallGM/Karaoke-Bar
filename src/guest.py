class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay_entry_fee(self, room):
        fee = room.entry_fee
        if fee <= self.wallet:
            self.wallet -= fee
            return True
        else:
            return False
