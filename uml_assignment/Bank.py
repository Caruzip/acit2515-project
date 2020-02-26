from BankStats import BankStats

class Bank:
    """holds all accounts made"""
    def __init__(self, name):
        """ Init instance attributes and validation of parameters"""

        if type(name) != str:
            raise ValueError("The name must be a string. ")

        self._name = name
        self._accounts = []

    def get_name(self):
        """returns the name of the bank"""
        return self._name

    def add_account(self, account):
        """adds an account to the bank"""
        self._accounts.append(account)

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
        if type != 'savings' and type != 'chequing':
            raise ValueError("account must be either chequing or savings")
        else:
            for account in self._accounts:
                if account.get_type() == type:
                    accounts.append(account)

            return accounts

    def delete_account(self, id):
        """removes an account with the associated id"""
        for account in self._accounts:
            if account.get_account_id() == id:
                self._accounts.remove(account)

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


