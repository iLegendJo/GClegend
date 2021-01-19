class Beverage:

    def __init__(self, bev__name):
        self.__bev_name = bev__name

    def get_bev_name(self):
        return self.__bev_name


class Cola(Beverage):

    def __init__(self):
        Beverage.__init__(self, 'cola')

    def __str__(self):
        return self.get_bev_name()


def main():
    drink1 = Cola()
    print(drink1)


if __name__ == "__main__":
    main()