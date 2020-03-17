from BankStats import BankStats
import json
from Chequing import Chequing
from Savings import Savings
import os.path


class Bank:
    """holds all accounts made"""
    def __init__(self, name):
        """ Init instance attributes and validation of parameters"""

        if type(name) != str:
            raise ValueError("The name must be a string. ")

        self._name = name
        self._accounts = []
        self._filepath = "./entities/bank.json"
        self._read_from_file()

    def get_name(self):
        """returns the name of the bank"""
        return self._name

    def add_account(self, account):
        """adds an account to the bank"""
        self._accounts.append(account)
        self._write_to_file("append", account)

    def get_account_id(self, account_id):
        """returns the account with the associated id"""
        for account in self._accounts:
            if account.get_account_id() == account_id:
                return account

    def get_all(self):
        """returns all accounts"""
        return self._accounts

    def get_all_by_type(self, type):
        """returns a list of all accounts with the inputted type"""
        accounts = []
        for account in self._accounts:
            if account.get_type() == type:
                accounts.append(account)

        if type != "chequing":
            if type != "savings":
                raise ValueError(f"Bank does not carry {type} accounts")

        return accounts

    def delete_account(self, id):
        """removes an account with the associated id"""
        if not self.get_account_id(id):
            raise ValueError(f"Account with id: {id} doesn't exist")
        for account in self._accounts:
            if account.get_account_id() == id:
                self._accounts.remove(account)
                self._write_to_file("delete", account)

    def update_chequing(self, id, fname=False, lname=False, fees=False, rebate="", min_balance=False):
        """updates a chequing account"""
        account = self.get_account_id(id)
        if not account:
            raise ValueError(f"Account with id: {id} does not exist")

        if fname:
            account.set_fname(fname)
        if lname:
            account.set_lname(lname)

        if fees:
            account.set_fees(fees)
        if rebate == True or rebate == False:
            account.set_rebate(rebate)
        if min_balance:
            account.set_min(min_balance)
        self._write_to_file("update", account)

    def update_savings(self, id, fname=False, lname=False, interest=False):
        """updates a savings account"""
        account = self.get_account_id(id)
        if not account:
            raise ValueError(f"Account with id: {id} does not exist")

        if fname:
            account.set_fname(fname)
        if lname:
            account.set_lname(lname)

        if interest:
            account.new_interest(interest)
        self._write_to_file("update", account)

    def get_stats(self):
        """creates an instance of BankStats with current account stats"""
        savings_accounts = self.get_all_by_type('savings')
        chequing_accounts = self.get_all_by_type('chequing')
        balance = 0
        c_balance = 0
        s_balance = 0
        owners = []
        for account in self._accounts:
            name = account.get_first_name() + account.get_last_name()
            balance += account.get_total_balance()
            if name not in owners:
                owners.append(account)

        for account in savings_accounts:
            s_balance += account.get_total_balance()

        for account in chequing_accounts:
            c_balance += account.get_total_balance()

        return BankStats(len(self._accounts), len(savings_accounts), len(chequing_accounts),
                         len(owners), balance, s_balance, c_balance)

    def _read_from_file(self):
        """reads from the bank.json file and adds existing classes to the bank"""
        if os.path.exists(self._filepath):
            with open(self._filepath) as f:
                data = json.load(f)
            for account in data["chequing"]:
                c = Chequing(account['account_id'], account['fname'],
                             account['lname'], account['fees'],
                             account['rebate'], account['min_balance'],
                             account['balance'], account['transactions'])
                self._accounts.append(c)
            for account in data["savings"]:
                s = Savings(account['account_id'], account['fname'],
                            account['lname'], account['interest'],
                            account['date_interest'], account['balance'],
                            account['transactions'])
                self._accounts.append(s)
        else:
            if os.path.exists("./entities"):
                data = {"chequing": [], "savings": []}
                with open(self._filepath, 'w') as bank:
                    json.dump(data, bank)
            else:
                os.mkdir("./entities")
                data = {"chequing": [], "savings": []}
                with open(self._filepath, 'w') as bank:
                    json.dump(data, bank)

    def _write_to_file(self, task, account):
        """add/delete/update the json file to store information about the accounts in the bank"""
        f = open(self._filepath)
        data = json.load(f)
        if task == "delete":
            id = account.get_account_id()

            for l in data["chequing"]:
                if l["account_id"] == id:
                    data["chequing"].remove(l)

            for l in data["savings"]:
                if l["account_id"] == id:
                    data["savings"].remove(l)

            json.dumps(data)
            with open(self._filepath, 'w') as bank:
                json.dump(data, bank)

        elif task == "append":
            if account.get_type() == "savings":
                acc = account.to_dict()
                data["savings"].append(acc)
            elif account.get_type() == "chequing":
                data["chequing"].append(account.to_dict())
            json.dumps(data)
            with open(self._filepath, 'w') as bank:
                json.dump(data, bank)

        elif task == "update":
            id = account.get_account_id()
            for l in data["chequing"]:
                if l["account_id"] == id:
                    data["chequing"].remove(l)
                    data["chequing"].append(account.to_dict())

            for l in data["savings"]:
                if l["account_id"] == id:
                    data["savings"].remove(l)
                    data["savings"].append(account.to_dict())

            json.dumps(data)
            with open(self._filepath, 'w') as bank:
                json.dump(data, bank)
        f.close()

