from src.guest import Guest
from src.room import Room
import unittest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Patrick", 20, "Imagine")
        self.room = Room(5, 10)
        self.room_2 = Room(5, 30)

    def test_guest_has_name(self):
        self.assertEqual("Patrick", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual(20, self.guest.wallet)

    def test_guest_can_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.room)
        self.assertEqual(10, self.guest.wallet)

    def test_guest_cannot_pay_if_no_money(self):
        self.assertEqual(False, self.guest.pay_entry_fee(self.room_2))
        self.assertEqual(20, self.guest.wallet)
