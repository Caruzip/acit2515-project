from .AbstractAccount import AbstractAccount
from peewee import FloatField, DateField


class Savings(AbstractAccount):
    interest = FloatField()
    date_interest = DateField()
    ACCOUNT_TYPE = 'savings'

    def to_dict(self):
        """ Returns dictionary of instance state """
        output = dict()
        output["account_id"] = self.id
        output["fname"] = self.first_name
        output["lname"] = self.last_name
        output["type"] = self.ACCOUNT_TYPE
        output["interest"] = self.interest
        output["date_interest"] = self.date_interest
        output["balance"] = self.total_balance
        output["transactions"] = self.transactions
        return output

