def question_one():
    try:

        with open("Popular_Baby_Names.csv", "r") as file_object:
            next(file_object)
            lines = [line.strip().split(",") for line in file_object if line.strip().split(",")[0] == "2013" and line.strip().split(",")[3] == "Zoey" and line.strip().split(",")[2] == "HISPANIC"]
        return lines
    except FileNotFoundError:
        print("The file not found")
    except:
        print("all other errors")


x = question_one()
print(x)