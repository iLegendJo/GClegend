class Baby():

    def __init__(self, birth_year, gender,ethnicity,first_name, count, rank):
        self.__birth_year = birth_year
        self.__gender = gender
        self.__ethnicity = ethnicity
        self.__first_name = first_name
        self.__count = count
        self.__rank = rank

    def get_birth_year(self):
        return self.__birth_year

    def set_birth_year(self,birth_year):
        self.__birth_year = birth_year

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender

    def get_ethnicity(self):
        return self.__gender

    def set_ethnicity(self,ethnicity):
        self.__ethnicity = ethnicity

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self,first_name):
        self.__first_name = first_name

    def get_count(self):
        return self.__count

    def set_count(self,count):
        self.__count = count

    def get_rank(self):
        return self.__rank

    def set_rank(self,rank):
        self.__rank = rank

    def __str__(self):
        return self.__init__(2016,"Female","ASIAN AND PACIFIC ISLANDER","Olivia",172, 1)


def main():

    with open("Popular_Baby_Names.csv", "r") as file_object:
        next(file_object)
        lines = [line.strip().split(",") for line in file_object]
        employee_look_up = {}
        for row in lines:
            print(row)


if __name__ == "__main__":
    main()
