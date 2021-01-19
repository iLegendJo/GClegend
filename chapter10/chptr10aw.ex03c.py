class BankAccount():

    def __init__(self, account_number, balance, deposit, withdraw):
        self.account_number = account_number
        self.balance = balance
        self.deposit = deposit
        self.interest = 0
        self.withdraw = withdraw

    # ***********************************************************************************
    # defining Accessor method or Getter Methods

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def get_deposit(self):
        return self.deposit

    def get_interest(self):
        return self.interest

    def get_withdraw(self):
        return self.withdraw

    def __str__(self):
       #return the state of the book object
        return "Account number: "+ str(self.account_number) + " " + "Balance: " + str(self.balance) + " " \
               + "Deposit: " + str(self.deposit) + " " + "Interest:  "+ str(self.interest) + " " +\
               "withdraw" + " " + str(self.withdraw)

    # ***************************************************************************************
    def set_account_number(self,account_number):
        self.account_number = account_number

    def set_balance(self, balance):
        self.balance = balance

    def set_deposit(self, deposit):
        self.balance = self.balance + deposit
        self.deposit = deposit

    def set_interest(self,interest):
        self.interest = self.interest * interest
        self.interest = interest

    def set_withdraw(self, withdraw):
        self.withdraw = withdraw


def main():

    bank_account1 = BankAccount(1, 500.50,100,150)
    # bank_account1.set_account_number(5)
    print(bank_account1)


if __name__ == "__main__":
        main()