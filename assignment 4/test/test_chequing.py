from unittest import TestCase
from models.Chequing import Chequing
from peewee import SqliteDatabase

db = SqliteDatabase('bank.sqlite', pragmas={'foreign_keys': 1})
db.connect()

class TestChequing(TestCase):
    """ Unit tests for the Chequing Class """

    def setUp(self):
        self.test_c = Chequing(first_name="bob", last_name="smith",
                               fees=3.00,
                               rebate=True,
                               min_balance=500.00)

    def test_chequing(self):
        """ 110A - Valid Construction """
        self.assertIsNotNone(self.test_c, "Chequing account must be defined.")
        self.assertIsInstance(self.test_c, Chequing)

    def test_to_dict(self):
        """118A - valid dictionary """
        self.assertEqual(type(self.test_c.to_dict()), type({"dict": "dictionary"}))


