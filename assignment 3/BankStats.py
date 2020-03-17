
class BankStats:
    """stats about the Bank"""
    def __init__(self, accounts, total_s, total_c, total_owners, total_balance,
                 total_s_balance, total_c_balance):
        self._total_accounts = accounts
        self._total_s_accounts = total_s
        self._total_c_accounts = total_c
        self._total_owners = total_owners
        self._total_balance = total_balance
        self._total_s_balance = total_s_balance
        self._total_c_balance = total_c_balance

    def get_total_accounts(self):
        """returns the total number of accounts"""
        return self._total_accounts

    def get_total_s_accounts(self):
        """returns the total number of savings accounts"""
        return self._total_s_accounts

    def get_total_c_accounts(self):
        """returns the total number of chequing accounts"""
        return self._total_c_accounts

    def get_total_owners(self):
        """returns the number of customers with accounts on the Bank"""
        return self._total_owners

    def get_total_balance(self):
        """returns the total balance of all accounts in the Bank"""
        return self._total_balance

    def get_total_s_balance(self):
        """returns the total balance of all savings account in the bank"""
        return self._total_s_balance

    def get_total_c_balance(self):
        """returns the total balance of all chequing accounts in the bank"""
        return self._total_c_balance

    def to_dict(self):
        """converts object to dictionary to convert to JSON"""
        return {"total_accounts": self._total_accounts, "total_s_accounts": self._total_s_accounts,
                "total_c_accounts": self._total_c_accounts, "owners": self._total_owners,
                "total_balance": self._total_balance, "total_savings": self._total_s_balance,
                "total_chequing": self._total_c_balance}