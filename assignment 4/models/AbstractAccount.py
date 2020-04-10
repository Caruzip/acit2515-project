from abc import ABC
from abc import abstractmethod
from peewee import SqliteDatabase, Model, IntegerField, CharField, FloatField
from abc import abstractmethod

db = SqliteDatabase('bank.sqlite', pragmas={'foreign_keys': 1})
db.connect()


class AbstractAccount(Model):
    first_name = CharField()
    last_name = CharField()
    total_balance = FloatField(default=0)
    transactions = IntegerField(default=0)

    def __eq__(self, other):
        name = self.first_name + self.last_name
        othername = other.first_name + other.last_name
        return name == othername

   # @property
    #def account_id(self):
    #    return self.id

    def deposit(self, amount):
        self.total_balance += amount
        self.transactions += 1
        self.save()

    def withdraw(self, amount):
        self.total_balance -= amount
        self.transactions += 1
        self.save()

    @abstractmethod
    def to_dict(self):
        """change object to dictionary"""
        raise NotImplementedError("Child must Implement abstract method")

    class Meta:
        database = db





