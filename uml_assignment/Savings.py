from AbstractAccount import AbstractAccount
import datetime


class Savings(AbstractAccount):
    """creates a savings account"""
    ACCOUNT_TYPE = 'savings'

    def __init__(self, account_id, fname, lname, interest):
        """ Init instance attributes and validation of parameters"""

        if type(interest) != float or interest < 0:
            raise ValueError("The interest must be a positive float")

        self._interest = interest
        self._date_interest = datetime.datetime.now()

        AbstractAccount.__init__(self, account_id, fname, lname)

    def get_type(self):
        """returns savings"""
        return self.ACCOUNT_TYPE

    def get_details(self):
        """gets the details of the account"""
        details = f"Details"
        return details

    def get_interest(self):
        """returns the interest"""
        return self._interest

    def get_total_balance(self):
        """returns the total balance of the account"""
        return self._total_balance

    def set_interest(self, interest):
        """sets interest"""
        self._interest = interest
        self._date_interest = datetime.datetime.now()

