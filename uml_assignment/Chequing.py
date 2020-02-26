from AbstractAccount import AbstractAccount


class Chequing(AbstractAccount):
    """creates an instance of abstract account as a chequing account"""
    ACCOUNT_TYPE = 'chequing'

    def __init__(self, account_id, fname, lname, fees, rebate, min_balance):
        """ Init instance attributes and validation of parameters"""

        if type(rebate) != bool:
            raise ValueError("The rebate must be true  or false. ")

        if type(fees) != float or fees < 0:
            raise ValueError("The monthly fees must be a positive float")

        if type(min_balance) != float or min_balance < 0:
            raise ValueError("The min balance must be a positive float")

        self._monthly_fees = fees
        self._is_rebate = rebate
        self._min_balance = min_balance

        AbstractAccount.__init__(self, account_id, fname, lname)

    def get_type(self):
        """returns chequing"""
        return self.ACCOUNT_TYPE

    def get_details(self):
        """gets the details of the account"""
        details = f"Details"
        return details

    def rebate_calc(self):
        """calculates the rebate and adds money back into user's account"""
        if not self._is_rebate:
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
        return self._is_rebate




