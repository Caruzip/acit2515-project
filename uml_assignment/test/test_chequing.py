from unittest import TestCase
from Chequing import Chequing


class TestChequing(TestCase):
    """ Unit tests for the Chequing Class """

    def setUp(self):
        self.test_c = Chequing(10, "bob", "smith", 3.00, True, 500.00)

    def test_chequing(self):
        """ 110A - Valid Construction """
        self.assertIsNotNone(self.test_c, "Chequing account must be defined.")
        self.assertIsInstance(self.test_c, Chequing)

    def test_chequing_invalid_parameters(self):
        """ 110B - Invalid Construction Parameters """
        with self.assertRaises(ValueError):
            Chequing(10, 4, "smith", 3.00, True, 500)

    def test_get_type(self):
        """ 111A - Valid return type """
        self.assertEqual(self.test_c.get_type(), "chequing")

    def test_get_details(self):
        """ 112A - Valid return of details """
        self.assertEqual(type(self.test_c.get_details()), str)

    def test_rebate_calc(self):
        """ 113A - Valid Calculation"""
        self.test_c.deposit(600.00)
        self.test_c.rebate_calc()
        self.assertEqual(self.test_c._total_balance, 600.00)

    def test_get_monthly_fees(self):
        """ 114A - Valid return of get monthly fees """
        self.assertEqual(self.test_c.get_monthly_fees(), 3.00)

    def test_get_total_balance(self):
        """115A - Valid return total balance """
        self.test_c.deposit(600.00)
        self.assertEqual(self.test_c.get_total_balance(), 600.00)

    def test_get_min_balance(self):
        """ 116A - Valid return of min balance"""
        self.assertEqual(self.test_c.get_min_balance(), 500.00)

    def test_get_is_rebate(self):
        """ 117A - Valid return of is rebate"""
        self.assertEqual(self.test_c.is_rebate(), True)
