from flask import jsonify
from .Chequing import Chequing
from .Savings import Savings
from peewee import SqliteDatabase, Model, IntegerField, CharField, FloatField
from BankStats import BankStats
from datetime import datetime

db = SqliteDatabase('bank.sqlite', pragmas={'foreign_keys': 1})
db.connect()


class Bank:
    """holds all accounts made"""
    def __init__(self, name):
        """ Init instance attributes and validation of parameters"""

        if type(name) != str:
            raise ValueError("The name must be a string. ")

        self._name = name
        self.savings_accounts = self.get_all_by_type("savings")
        self.chequing_accounts = self.get_all_by_type("chequing")

    def get_name(self):
        """returns the name of the bank"""
        return self._name

    def add_account(self, account):
        """saves account to the database"""
        if isinstance(account, Chequing):
            atype = "chequing"
        else:
            atype = "savings"

        accounts = self.get_all()
        account_id = len(accounts) + 1

        for i in accounts:
            if account == i:
                raise ValueError("user can only have 1 chequing account and 1 savings account")

        if account_id == 1:
            account.save()
            return 1
        else:
            account.save()
            aid = account.id

            if atype == "savings":
                query = Savings.update(id=account_id).where(Savings.id == aid)
                query.execute()

            elif atype == "chequing":
                query = Chequing.update(id=account_id).where(Chequing.id == aid)
                query.execute()

    def get_account_id(self, account_id):
        """returns the account with the associated id"""
        acc = 0
        accounts = self.get_all()
        for i in accounts:
            if i.id == account_id:
                acc = i
        if acc:
            return acc
        else:
            raise ValueError(f"account with id: {account_id} does not exist")

    def get_all(self):
        """returns all accounts"""
        accounts = []
        [accounts.append(i) for i in Savings.select()]
        [accounts.append(i) for i in Chequing.select()]
        return accounts

    def get_all_by_type(self, type):
        """returns a list of all accounts with the inputted type"""
        accounts = []
        if type == "savings":
            [accounts.append(i) for i in Savings.select()]
        elif type == "chequing":
            [accounts.append(i) for i in Chequing.select()]
        else:
            return ValueError(f"Bank does not carry account type {type}")

        return accounts

    def delete_account(self, id):
        """removes an account with the associated id"""
        try:
            account_delete = self.get_account_id(id)
            account_delete.delete_instance()

        except ValueError as e:
            print(e)

    def update_chequing(self, account, data):
        """updates a chequing account"""

        for i in data.keys():
            if i == 'fname':
                query = Chequing.update(first_name=data['fname']).where(Chequing.id == account.id)
                query.execute()
            elif i == 'lname':
                query = Chequing.update(last_name=data['lname']).where(Chequing.id == account.id)
                query.execute()
            elif i == 'fees':
                num = float(data['fees'])
                query = Chequing.update(fees=num).where(Chequing.id == account.id)
                query.execute()
            elif i == 'rebate':
                if data['rebate'] == 'False':
                    value = 0
                else:
                    value = 1
                query = Chequing.update(rebate=value).where(Chequing.id == account.id)
                query.execute()
            elif i == 'min_balance':
                num = float(data['min_balance'])
                query = Chequing.update(min_balance=num).where(Chequing.id == account.id)
                query.execute()

    def update_savings(self, account, data):
        """updates a savings account"""

        for i in data.keys():
            if i == 'fname':
                query = Savings.update(first_name=data['fname']).where(Savings.id == account.id)
                query.execute()
            elif i == 'lname':
                query = Savings.update(last_name=data['lname']).where(Savings.id == account.id)
                query.execute()
            elif i == 'interest':
                num = float(data['interest'])
                query = Savings.update(interest=num).where(Savings.id == account.id)
                query.execute()
                query = Savings.update(date_interest=datetime.now()).where(Savings.id == account.id)
                query.execute()

    def get_stats(self):
        """creates an instance of BankStats with current account stats"""
        savings_accounts = self.get_all_by_type('savings')
        chequing_accounts = self.get_all_by_type('chequing')
        balance = 0
        c_balance = 0
        s_balance = 0
        owners = []
        accounts = 0
        for account in self.get_all():
            name = account.first_name + account.last_name
            balance += account.total_balance
            accounts += 1
            if name not in owners:
                owners.append(name)

        for account in savings_accounts:
            s_balance += account.total_balance

        for account in chequing_accounts:
            c_balance += account.total_balance

        return BankStats(accounts, len(savings_accounts), len(chequing_accounts),
                         len(owners), balance, s_balance, c_balance)

    class Meta:
        database = db



