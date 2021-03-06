class Employee:

    def __init__(self,employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def get_employee_number(self):
        return self.__employee_number

    def set_employee_number(self,employee_number):
        self.__employee_number = employee_number


class ProductionWorker(Employee):
    def __init__(self,employee_name, employee_number, shift_number,hourly_pay_rate):
        Employee.__init__(self,employee_name,employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def set_shift_number(self,shift_number):
        self.__shift_number = shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_hourly_pay_rate(self,hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def __str__(self):
        #  return the state of the production_worker1 object
        return self.employee_name + " "+ self.__shift_number + " " + str(self.__hourly_pay_rate)


def main():
    employee_number = input("Please enter your employee number: ")
    employee_name = input("Please enter your name: ")
    user_shift_number = input("please enter a shift number: ")
    user_hourly_pay = input("Please enter your hourly rate: ")
    production_worker1 = ProductionWorker(employee_number,employee_name, user_shift_number,user_hourly_pay)
    print(production_worker1)


if __name__ == "__main__":
    main()