from unittest import TestCase
from Bank import Bank
from BankStats import BankStats
from Savings import Savings


class TestBank(TestCase):
    """ Unit tests for the Bank Class """

    def setUp(self):
        self.test_b = Bank("CIT Bank")
        self.test_a = Savings(10, 'bob', 'smith', 2.0)

    def test_bank(self):
        """ 110A - Valid Construction """
        self.assertIsNotNone(self.test_b, "Bank must be defined.")
        self.assertIsInstance(self.test_b, Bank)

    def test_bank_invalid_parameters(self):
        """ 110B - Invalid Construction Parameters """
        with self.assertRaises(ValueError):
            Bank(34)

    def test_get_name(self):
        """ 111A - Get valid name value """
        self.assertEqual(self.test_b.get_name(), "CIT Bank")

    def test_add_account(self):
        """112A - Checks valid adding of account"""
        self.test_b.add_account(self.test_a)
        self.assertEqual(len(self.test_b._accounts), 1)

    def test_get_account_id(self):
        """ 113A - Get valid account by id """
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_account_id(10)), type(self.test_a))

    def test_get_all(self):
        """ 115A - Get all accounts """
        self.test_b.add_account(self.test_a)
        self.assertEqual(self.test_b.get_all(), [self.test_a])

    def test_get_all_by_type(self):
        """ 116A - Get all accounts by type"""
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_all_by_type("savings")), type([]))

    def test_get_all_by_type_invalid(self):
        """ 116B - Invalid Get all accounts by type"""
        with self.assertRaises(ValueError):
            self.test_b.get_all_by_type(3)

    def test_delete_account(self):
        """ 117A - Valid deletion of account"""
        self.test_b.add_account(self.test_a)
        self.test_b.delete_account(10)
        self.assertEqual(len(self.test_b._accounts), 0)

    def test_get_stats(self):
        """ 118A - Valid object returned """
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_stats()), BankStats)
