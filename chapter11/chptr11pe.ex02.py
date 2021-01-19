import employee


class ShiftSupervisor(employee.Employee):
    def __init__(self, annual_salary, annual_bonus):
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def set_annual_salary(self, annual_salary):
         self.__annual_salary = annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def __str__(self):
        return employee.get_employee_number() + " " + employee.get_employee_name() + "  " + self.__annual_salary +\
               " " + self.__annual_bonus


def main():

    shift_supervisor1 = ShiftSupervisor("1","James Brown",100,200)
    print(shift_supervisor1)

    if __name__ == "__main__":
        main()
