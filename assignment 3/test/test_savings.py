from unittest import TestCase
from Savings import Savings


class TestSavings(TestCase):
    """ Unit tests for the Savings Class """

    def setUp(self):
        self.test_s = Savings(10, 'bob', 'smith', 2.0, "1990-01-01")

    def test_bank(self):
        """ 110A - Valid Construction """
        self.assertIsNotNone(self.test_s, "Savings account must be defined.")
        self.assertIsInstance(self.test_s, Savings)

    def test_bank_invalid_parameters(self):
        """ 110B - Invalid Construction Parameters """
        with self.assertRaises(ValueError):
            Savings("adsf", 'bob', 'smith', 2.0, "1099-03-21")

    def test_get_type(self):
        """ 111A - Valid return type """
        self.assertEqual(self.test_s.get_type(), "savings")

    def test_get_details(self):
        """ 112A - Valid return of details """
        self.assertEqual(type(self.test_s.get_details()), str)

    def test_get_total_balance(self):
        """113A - Valid return total balance """
        self.test_s.deposit(600.00)
        self.assertEqual(self.test_s.get_total_balance(), 600.00)

    def test_set_interest(self):
        """114A - valid setting of interest """
        self.test_s.set_interest(2.55)
        self.assertEqual(self.test_s.get_interest(), 2.55)

    def test_to_dict(self):
        """115A - valid to dict """
        self.assertEqual(type(self.test_s.to_dict()), type({"dict": "dictionary"}))

