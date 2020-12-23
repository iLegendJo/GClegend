def display_q02(lines,gender):
    try:
        max_value = 0
        max_name = ""
        for line in lines:
            name = line[3]
            count = int(line[4])
            if line[1] == gender:
                if count > max_value:
                    max_value = count  # contains the highest value when found check to see if higher than previous count
                    max_name = name  # associate max value with the name.
    except IndexError:
        print("out of range ")
    return {"name":max_name,"count":max_value}


def main():

    try:

        with open("Popular_Baby_Names.csv", "r") as file_object:
            next(file_object)

            lines = [line.strip().split(",") for line in file_object if
                     line.strip().split(",")[0] == '2015' and line.strip().split(",")[2] == "ASIAN AND PACIFIC ISLANDER"]

            female_display = display_q02(lines,"FEMALE")
            print(female_display)
            male_display = display_q02(lines,"MALE")
            print(male_display)
    except FileNotFoundError:
        print("File not found please check filename")


if __name__ == "__main__":
    main()