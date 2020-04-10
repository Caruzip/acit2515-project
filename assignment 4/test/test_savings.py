from unittest import TestCase
from models.Savings import Savings
from peewee import SqliteDatabase

db = SqliteDatabase('bank.sqlite', pragmas={'foreign_keys': 1})
db.connect()

class TestSavings(TestCase):
    """ Unit tests for the Savings Class """

    def setUp(self):
        self.test_s = Savings(first_name='bob', last_name='smith', interest=2.0, date_interest="1990-01-01")

    def test_bank(self):
        """ 110A - Valid Construction """
        self.assertIsNotNone(self.test_s, "Savings account must be defined.")
        self.assertIsInstance(self.test_s, Savings)

    def test_to_dict(self):
        """115A - valid to dict """
        self.assertEqual(type(self.test_s.to_dict()), type({"dict": "dictionary"}))

