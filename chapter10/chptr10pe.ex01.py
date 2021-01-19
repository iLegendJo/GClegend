class Pet:

    def __init__(self,name,animal_type,age):
        self.__name = name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        # defining Accessor method or Getter Methods
        return self.__name

    def set_name(self, name):
        # defining Mutator method or Setter Methods
        self.__name = name

    def get_animal_type(self,animal_type):
        return self.__animal_type

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def get_age(self,age):
        return self.__age

    def set_age(self,age):
        self.__age = age

    def __str__(self):
        # return the state of the book object
        return self.__name + " " + self.__animal_type + " " + self.__age


def main():
    input_name = input("Please enter Name: ")
    input_type = input("Please enter a type: ")
    input_age = input("Please enter a age: ")
    pet1 = Pet(input_name,input_type, input_age)
    print(pet1)
# pet1.set_age("15")


if __name__ == "__main__":
    main()