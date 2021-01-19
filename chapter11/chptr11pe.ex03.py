class Person:

    def __init__(self,name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone_number

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address

    def get_telephone_number(self):
        return self.__telephone_number

    def set_telephone_number(self,telephone_number):
        self.__telephone_number = telephone_number


class Customer(Person):
    def __init__(self,customer_number, mailing_mode):
        self.__customer_number = customer_number
        self.__mailing_mode = mailing_mode

    def get_customer_number(self,number):
        return self.__customer_number

    def set_customer_number(self,customer_number):
        self.__customer_number = customer_number

    def get_mailing_mode(self):
        return self.__mailing_mode

    def set_mailing_mode(self,mailing_mode):
        self.__mailing_mode = mailing_mode

    def __str__(self):
        return self.__customer_number + " "+ self.set_name("Julia Gold")


def main():

    customer1 = Customer("1", True)
    print(customer1)

    if __name__ == "__main__":
        main()


