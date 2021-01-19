import employee

employee_look_up = {}


def init():
    with open("employee_dictionary.csv", "r") as file_object:
        next(file_object)
        lines = [line.strip().split(",") for line in file_object]

        for row in lines:

            employee1 = employee.Employee(name=row[1], id_number=row[0], department=row[2], job_title=row[3])
            # print(employee1)
            employee_look_up[employee1.get_id_number()] = employee1


def look_up_menu():
    while True:

        employee_number = input("Please enter an employee number or Q to quit: ")

        if employee_number == "q":
            print("you have quit this program, Goodbye  ")
            return
        if employee_number in employee_look_up:
            employee_output = employee_look_up[employee_number]
        else:
            print(f"invalid id number, {employee_number}")
            continue
        print(employee_output)


def add_menu():

    while True:

        id_number = int(input("please enter your Id: "))
        name= input("please enter your name: ")
        department = input("please enter your Department: ")
        job_title = input("please enter your job title: ")
        emp = employee.Employee(name, id_number, department, job_title)
        print(emp)
        mode_add = input("Please enter Q to stop adding or A to continue adding")
        if mode_add == "Q":
            return


def update_menu():
    id_number = input("please enter your Id: ")
    current_emp = employee_look_up[id_number]
    print(current_emp)
    name = input("Please enter your name: ")
    department = input("Please enter your Department: ")
    job_title = input("Please enter your job title: ")
    current_emp.set_name(name)
    current_emp.set_department(department)
    current_emp.set_job_title(job_title)
    mode_add = input("Please enter Q to stop adding or A to continue adding")
    if mode_add == "Q":
        return


def delete_menu():
    id_number = input("please enter your Id: ")
    del employee_look_up[id_number]


def menu():
    while True:
        print("1: Look up mode:  ")
        print("2: add new employee ")
        print("3: change an existing employee's:")
        print("4: delete an employee")
        print("5: Quit:")
        mode = int(input("enter in mode:  "))
        if mode == 1:
            look_up_menu()
        if mode == 2:
            add_menu()
        if mode == 3:
            update_menu()
        if mode == 4:
            delete_menu()
        if mode == 5:
            print("you have quit this program, Goodbye  ")
            exit()


def main():
    init()
    menu()


if __name__ == "__main__":
    main()
