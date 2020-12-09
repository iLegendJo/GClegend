def display_05():

    with open("Popular_Baby_Names.csv", "r") as file_object:
        next(file_object)

        lines = [line.strip().split(",") for line in file_object if
                 line.strip().split(",")[1] =="MALE" and line.strip().split(",")[3].upper() == "DAVID"]
        line_two = [line for line in lines if line[2].find("WHITE NON HISP")> -1]

    return line_two


answer = display_05()
for result in answer:
    print(result)
#completed. last worked on 11.21.2020