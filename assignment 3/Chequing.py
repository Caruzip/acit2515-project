from AbstractAccount import AbstractAccount


class Chequing(AbstractAccount):
    """creates an instance of abstract account as a chequing account"""
    ACCOUNT_TYPE = 'chequing'

    def __init__(self, account_id, fname, lname, fees, rebate, min_balance, money=0, transactions=0):
        """ Init instance attributes and validation of parameters"""

        if type(rebate) != bool:
            raise ValueError("The rebate must be true  or false. ")

        if type(fees) != float or fees < 0:
            raise ValueError("The monthly fees must be a positive float")

        if type(min_balance) != float or min_balance < 0:
            raise ValueError("The min balance must be a positive float")

        self.set_fees(fees)
        self.set_rebate(rebate)
        self.set_min(min_balance)

        super().__init__(account_id, fname, lname, money, transactions)

    def set_fees(self, fees):
        """sets fees"""
        self._monthly_fees = fees

    def set_rebate(self, rebate):
        """sets rebate"""
        self._rebate = rebate

    def set_min(self, min):
        """sets min_balance"""
        self._min_balance = min

    def get_type(self):
        """returns chequing"""
        return self.ACCOUNT_TYPE

    def get_details(self):
        """gets the details of the account"""
        details = f"Details"
        return details

    def rebate_calc(self):
        """calculates the rebate and adds money back into user's account"""
        if not self._rebate:
            self._total_balance -= self._monthly_fees

    def get_monthly_fees(self):
        """finds the monthly fees associated with the account"""
        return self._monthly_fees

    def get_total_balance(self):
        """returns the total balance of the account"""
        return self._total_balance

    def get_min_balance(self):
        """returns the min balance of the account"""
        return self._min_balance

    def is_rebate(self):
        """returns true if account has rebate"""
        return self._rebate

    def to_dict(self):
        """converts object to dictionary"""
        return {"account_id": self._account_id, "fname": self._first_name,
                 "lname": self._last_name, "fees": self._monthly_fees,
                 "rebate": self._rebate, "min_balance": self._min_balance,
                "balance": self._total_balance, "transactions": self._transactions,
                "acc_type": "chequing"}





