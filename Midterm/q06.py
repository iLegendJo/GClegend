def display_06():

    with open("Popular_Baby_Names.csv", "r") as file_object:
        next(file_object)

        lines = [line.strip().split(",") for line in file_object ]
        line_two = [line for line in lines if line[5]== "1" and line[0] =="2016" ]
    return line_two


answer = display_06()
for result in answer:
    print(result)
#incomplete as of 2020.11.21