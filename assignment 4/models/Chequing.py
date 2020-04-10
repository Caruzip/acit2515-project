from .AbstractAccount import AbstractAccount
from peewee import FloatField, BooleanField


class Chequing(AbstractAccount):
    fees = FloatField()
    rebate = BooleanField()
    min_balance = FloatField()
    ACCOUNT_TYPE = 'chequing'

    def to_dict(self):
        """ Returns dictionary of instance state """
        output = dict()
        output["account_id"] = self.id
        output["fname"] = self.first_name
        output["lname"] = self.last_name
        output["type"] = self.ACCOUNT_TYPE
        output["monthly_fees"] = self.fees
        output["rebate"] = self.rebate
        output["min_balance"] = self.min_balance
        output["balance"] = self.total_balance
        output["transactions"] = self.transactions
        return output

    def rebate_calc(self):
        """calculates the rebate and adds money back into user's account"""
        if not self._rebate:
            self._total_balance -= self._monthly_fees

