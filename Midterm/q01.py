def question_one():

    with open("Popular_Baby_Names.csv", "r") as file_object:
        next(file_object)
        lines = [line.strip().split(",") for line in file_object if line.strip().split(",")[0] == "2013" and line.strip().split(",")[3] == "Zoey" and line.strip().split(",")[2] == "HISPANIC"]
    return lines

    print("The error is happening")


x = question_one()
print(x)