from unittest import TestCase, mock
from Bank import Bank
from BankStats import BankStats
from Savings import Savings
from Chequing import Chequing


class TestBank(TestCase):
    """ Unit tests for the Bank Class """

    def setUp(self):
        self.test_b = Bank("CIT Bank")
        self.test_a = Savings(10, 'bob', 'smith', 2.0, "1990-01-01")
        self.test_c = Chequing(12, 'bob', 'smith', 50.0, False, 200.0)

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

    def test_get_account_id(self):
        """ 113A - Get valid account by id """
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_account_id(10)), type(self.test_a))

    def test_get_all_by_type(self):
        """ 116A - Get all accounts by type"""
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_all_by_type("savings")), type([]))

    def test_get_all_by_type_invalid(self):
        """ 116B - Invalid Get all accounts by type"""
        with self.assertRaises(ValueError):
            self.test_b.get_all_by_type(3)

    def test_get_stats(self):
        """ 118A - Valid object returned """
        self.test_b.add_account(self.test_a)
        self.assertEqual(type(self.test_b.get_stats()), BankStats)

    def test__init__(self):
        """ 119A - parameter validation for file path parameter """
        self.assertEqual(self.test_b._filepath, "./entities/bank.json")

    @mock.patch('Bank.Bank._read_from_file')
    def test_read_from_file(self, mock_read_func):
        """ 122A - checks if method is called but does nothing"""
        self.test_b._read_from_file()
        self.assertTrue(mock_read_func.called)

    @mock.patch('Bank.Bank._write_to_file')
    def test_write_to_file_add(self, mock_add_func):
        """ 130A - checks if method is called but does nothing"""
        self.test_b.add_account(self.test_a)
        self.assertTrue(mock_add_func.called)

    @mock.patch('Bank.Bank._write_to_file')
    def test_write_to_file_delete(self, mock_delete_func):
        """ 130B - checks if method is called but does nothing"""
        self.test_b.add_account(self.test_a)
        self.test_b.delete_account(10)
        self.assertTrue(mock_delete_func.called)


