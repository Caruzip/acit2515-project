from unittest import TestCase, mock
from models.Bank import Bank
from BankStats import BankStats
from models.Savings import Savings
from models.Chequing import Chequing
from peewee import SqliteDatabase

db = SqliteDatabase('bank2.sqlite', pragmas={'foreign_keys': 1})
db.connect()


class TestBank(TestCase):
    """ Unit tests for the Bank Class """

    def setUp(self):
        """ Tests table creation"""
        db.create_tables([Chequing, Savings])
        self.test_b = Bank(name="CIT Bank")
        self.test_a = Savings(first_name='bob', last_name='smith',
                              interest=2.0, date_interest="1990-01-01")
        self.test_c = Chequing(first_name='bob', last_name='smith',
                               fees=50.0, rebate=False, min_balance=200.0)

    def tearDown(self):
        """Tests table drop"""
        db.drop_tables([Chequing, Savings])

    def test_bank(self):
        """ 110A - Valid Construction """
        self.assertIsNotNone(self.test_b, "Bank must be defined.")
        self.assertIsInstance(self.test_b, Bank)

    def test_bank_invalid_parameters(self):
        """ 110B - Invalid Construction Parameters """
        with self.assertRaises(ValueError):
            Bank(name=34)

    def test_get_name(self):
        """ 111A - Get valid name value """
        self.assertEqual(self.test_b.get_name(), "CIT Bank")

    def test_get_account_id(self):
        """ 113A - Get valid account by id """
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_account_id(1)), type(self.test_a))

    def test_get_all_by_type(self):
        """ 116A - Get all accounts by type"""
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_all_by_type("savings")), type([]))

    def test_get_stats(self):
        """ 118A - Valid object returned """
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_stats()), BankStats)




