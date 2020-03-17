from AbstractAccount import AbstractAccount
import datetime


class Savings(AbstractAccount):
    """creates a savings account"""
    ACCOUNT_TYPE = 'savings'

    def __init__(self, account_id, fname, lname, interest, date, money=0, transactions=0):
        """ Init instance attributes and validation of parameters"""

        if type(interest) != float or interest < 0:
            raise ValueError("The interest must be a positive float")

        self.set_interest(interest)
        self.set_date_interest(date)

        super().__init__(account_id, fname, lname, money, transactions)

    def set_interest(self, interest):
        """sets interest"""
        self._interest = interest

    def set_date_interest(self, date):
        """sets the interest date"""
        self._date_interest = date

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

    def new_interest(self, interest):
        """sets interest"""
        self._interest = interest
        self._date_interest = str(datetime.datetime.now())

    def get_date_interest(self):
        """gets the date of interest"""
        return self._date_interest

    def to_dict(self):
        """converts object to dictionary"""
        return {"account_id": self._account_id, "fname": self._first_name,
                "lname": self._last_name, "interest": self._interest,
                "date_interest": self._date_interest, "balance": self._total_balance,
                "transactions": self._transactions, "acc_type": "savings"}

