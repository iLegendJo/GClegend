class Car:

    def __init__(self,year_model,make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def set_year_model(self,year_model):
        self.__year_model = year_model

    def get_make(self):
        return self.__make

    def set_make(self,make):
        self.__make = make

    def get_speed(self):
        return self.__speed

    def set_speed(self,speed):
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def __str__(self):
        return "year Model: "+self.__year_model + " Make: " + self.__make + " Speed:" + str(self.__speed)


def main():

    car1 = Car("1998", "Lexus")
    car1.set_speed(89)
    car1.brake()
    car1.accelerate()
    print(car1)


if __name__ == "__main__":
    main()



