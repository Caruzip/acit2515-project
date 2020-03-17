from abc import ABC
from abc import abstractmethod


class AbstractAccount(ABC):
    """creates a bank account object"""

    def __init__(self, account_id, fname, lname, money, transactions):
        """ Init instance attributes and validation of parameters"""

        if type(account_id) != int or (account_id < 0):
            raise ValueError("The account id must be a positive integer")

        if type(fname) != str or type(lname) != str:
            raise ValueError("The first and last name must be a string.")

        self.set_id(account_id)
        self.set_fname(fname)
        self.set_lname(lname)
        self._total_balance = money
        self._transactions = transactions

    def set_id(self, id):
        """sets id"""
        self._account_id = id

    def set_fname(self, fname):
        """sets first name"""
        self._first_name = fname

    def set_lname(self, lname):
        """sets last name"""
        self._last_name = lname

    def get_account_id(self):
        """returns account id"""
        return self._account_id

    def get_first_name(self):
        """returns the first name associated with the account"""
        return self._first_name

    def get_last_name(self):
        """returns last name associated with the account"""
        return self._last_name

    def get_total_balance(self):
        """returns total balance of the account"""
        return self._total_balance

    @abstractmethod
    def get_type(self):
        """returns type"""
        raise NotImplementedError("Child must Implement abstract method")

    @abstractmethod
    def get_details(self):
        """returns details"""
        raise NotImplementedError("Child must Implement abstract method")

    def withdraw(self, amount):
        """withdraw money out of the account"""
        self._total_balance = self._total_balance - amount

    def deposit(self, amount):
        """deposit money into the account"""
        self._total_balance = self._total_balance + amount

    @abstractmethod
    def to_dict(self):
        """change object to dictionary"""
        raise NotImplementedError("Child must Implement abstract method")




