def display_06():
    try:
        with open("Popular_Baby_Names.csv", "r") as file_object:
            next(file_object)

            lines = [line.strip().split(",") for line in file_object ]
            line_two = [line for line in lines if line[5]== "1" and line[0] =="2016" ]
        return line_two

    except FileNotFoundError:
        print("The file not found")
    except:
        print("all other errors")


answer = display_06()
for result in answer:
    print(result)
#incomplete as of 2020.11.21