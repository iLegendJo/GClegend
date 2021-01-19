class Plant:

    def __init__(self, plant_type):
        self.__plant_type = plant_type

    def message(self):
        print("I am a Plant." + self.__plant_type)


class Tree(Plant):
    def __init__(self):
        Plant.__init__(self,'tree')

    def message(self):
        print("I am a tree.")


def main():
    p = Plant('sapling')
    t = Tree() # tree - no print is being display
    p.message()  # I am a Plant
    t.message() # I am a three


if __name__ == '__main__':
    main()