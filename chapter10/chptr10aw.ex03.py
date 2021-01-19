class Customer:

    def __init__(self,account_number, first_name, middle_initial, last_name):
        self.__account_number = str(account_number)
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name

    def get_account_number(self):
        # get - assessor to the instance variable self.account_number
        return self.__account_number

    def get_first_name(self):
        # get - assessor to the instance variable self.first_name
        return self.first_name

    def get_middle_name(self):
        # get - assessor to the instance variable self.middle_initial
        return self.middle_initial

    def get_last_name(self):
        # get - assessor to the instance variable self.lastname
        return self.last_name

    def __str__(self):
        # return the state of the book object
        return self.__account_number+ " " + self.first_name+" "+ self.middle_initial + " " + self.last_name

    # ******************************************************************************

    def set_account_number(self, account_number):
        '''Assign a value to the instance variable account_number'''
        self.__account_number = account_number

    def set_first_name(self,first_name):
        '''Assign a value to the instance variable first_name'''
        self.first_name = first_name

    def set_middle_initial(self,middle_initial):
        '''Assign/mutator a value to the instance variable middle_intial'''
        self.middle_initial = middle_initial

    def set_last_name(self, last_name):
        '''Assign/mutator a value to the instance variable last_name'''
        self.last_name = last_name
# ******************************************************************************


def main():

    customer = Customer("1","Jane","E.", "Brown")
    customer.set_middle_initial("K")
    customer.set_account_number("2")
    customer.set_last_name("Stanley")
    print(customer)


if __name__ == "__main__":
    main()