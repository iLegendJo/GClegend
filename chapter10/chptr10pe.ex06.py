class Patient:

    def __init__(self, first_name, middle, last_name, address, city, state, zip_code, phone_number, emg__contact, emg_phone):
        self.__first_name = first_name
        self.__mid_name = middle
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emg_contact = emg__contact
        self.__emg_phone = emg_phone

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self,first_name):
        self.__first_name = first_name

    def get_mid_name(self):
        return self.__mid_name

    def set_mid_name(self,middle):
        self.__mid_name = middle

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self,last_name):
        self.__last_name = last_name

    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address

    def get_city(self):
        return self.__city

    def set_city(self,city):
        self.__city = city

    def get_state(self):
        return self.__state

    def set_state(self,state):
        self.__state = state

    def get_zip_code(self):
        return self.__zip_code

    def set_zip_code(self,zip_code):
        self.__zip_code = zip_code

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self,phone_number):
        self.__phone_number = phone_number

    def get_emg_contact(self):
        return self.__emg_contact

    def set_emg_contact(self,emg_contact):
        self.__emg_contact = emg_contact

    def get_emg_phone(self):
        return self.__emg_phone

    def set_emg_phone(self,emg_phone):
        self.__emg_phone = emg_phone

    def __str__(self):
        return self.__first_name + " " + self.__mid_name + " " + self.__last_name + " " + self.__address +\
               " " + self.__city + " " + self.__state + " " + self.__zip_code + " " + self.__phone_number + " " \
               + self.__emg_contact + " " + self.__emg_phone

    #*********************************************************************************************************************


def main():

    patient1 = Patient("Jay", "E.", "Brown", "130 East 99 Street","NY", "New York", "10159","917.214.1078","Jane","Roe")
    #print(patient1)


if __name__ == "__main__":
    main()


class Procedure:

    def __init__(self, name_of_procedure, date_of_procedure, name_of_practitioner, charges_of_procedure):
        self.__name_of_procedure = name_of_procedure
        self.__date_of_procedure = date_of_procedure
        self.__name_of_practitioner = name_of_practitioner
        self.__charges_of_procedure = float(charges_of_procedure)

    def get_name_of_procedure(self):
        return self.__name_of_procedure

    def set_name_of_procedure(self,name_of_procedure):
        self.__name_of_procedure = name_of_procedure

    def get_date_of_procedure(self):
        return self.__date_of_procedure

    def set_date_of_procedure(self,date_of_procedure):
        self.__date_of_procedure = date_of_procedure

    def get_name_of_practitioner(self):
        return self.__name_of_practitioner

    def set_name_of_practitioner(self,name_of_practitioner):
        self.__name_of_practitioner = name_of_practitioner

    def get_charges_of_procedure(self):
        return self.__charges_of_procedure

    def set_name_procedure(self,charges_of_procedure):
        self.__name_of_procedure = charges_of_procedure

    def __str__(self):
        return self.__name_of_procedure + " " + self.__date_of_procedure + " " + self.__name_of_practitioner + " " + \
               str(self.__charges_of_procedure)


def main():

    procedure1 = Procedure("Physical Exam", "December 29, 2020","Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", "December 29, 2020","Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood test", "December 29, 2020","Dr. Smith",200.00)

    my_list = [procedure1,procedure2,procedure3]
    total = 0
    #https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
    for num, current_row in enumerate(my_list,start=1):
        total = total + current_row.get_charges_of_procedure()
        print("Procedure #: {}: {}".format(num,current_row))
    print("total Charges:", total)


if __name__ == "__main__":
    main()



