class BankAccount():

    def __init__(self,account_number,opening_balance,deposit,credit,interest,back_charges,fees,closing_balance):
        self.account_number = float(account_number)
        self.opening_balance = float(opening_balance)
        self.deposit = float(deposit)
        self.credit = float(credit)
        self.interest = float(interest)
        self.back_charges = float(back_charges)
        self.fees = float(fees)
        self.closing_balance  = float(closing_balance)
    # ***********************************************************************************
    # defining Accessor method or Getter Methods

    def get_account_number(self):
        return self.account_number

    def get_opening_balance(self):
        return self.opening_balance

    def get_deposit(self):
        return self.deposit

    def get_credit(self):
        return self.credit

    def get_interest(self):
        return self.interest

    def get_back_charges(self):
        return self.back_charges

    def get_fees(self):
        return self.fees

    def get_closing_balance(self):
        return self.closing_balance

    def __str__(self):
        # return the state of the book object
        return str(self.account_number) + str(self.opening_balance) + " " + str(self.deposit() + " " + str(self.credit) + " " + str(self.interest)+
                                                                                " " + str(self.back_charges) + " " + str(self.fees) + " " + str(self.closing_balance))

    # ***************************************************************************************

    def set_account_number(self,account_number):
        self.account_number = account_number

    def set_opening_balance(self,opening_balance):
        self.opening_balance = opening_balance

    def set_deposit(self,deposit):
        self.deposit = deposit

    def set_credit(self,credit):
        self.credit = credit

    def set_interest(self,interest):
        self.interest = interest

    def set_back_charges(self,back_charges):
        self.back_charges = back_charges

    def set_fees(self,fees):
        self.fees = fees

    def set_closing_balance(self, closing_balance):
        self.closing_balance = closing_balance


def main():

    bank_account1 = BankAccount(1,50.00,100,28,.04,32,50,125)
    # bank_account1.set_account_number(4)
    print(bank_account1)



    if __name__ == "__main__":
        main()