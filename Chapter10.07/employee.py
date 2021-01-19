class Employee:

    def __init__ (self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = str(id_number)
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self,id_number):
        self.__id_number = id_number

    def get_department(self):
        return self.__department

    def set_department(self,department):
        self.__department = department

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self,job_title):
        self.__job_title = job_title

    def __str__(self):
        # return the state of the Employee object. this is only a display.
        return self.__name + " | " + self.__id_number + "|" + self.__department + " | " + self.__job_title


    #********************************************************************************************


def main():

    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    print(employee1)
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    print(employee2)
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    print(employee3)


if __name__ == "__main__":
    main()