def display_08():
    try:
        with open("Popular_Baby_Names.csv", "r") as file_object:
            next(file_object)

            lines = [line.strip().split(",") for line in file_object ]
            line_two = [line for line in lines if line[1] == "FEMALE" and line[3] == "Arianna" and line[0] == "2016"]
            max_number = int(line_two[0][4])
            max_line = line_two[0]
            size = len(line_two)
            # print(max_line)
            for i in range(1, size):
                # print(line_two[max_line])
                current_max = int(line_two[i][4])
                if current_max > max_number:
                    max_number = current_max
                    max_line = line_two[i]

        return max_line

    except FileNotFoundError:
        print("The file not found")
    except:
        print("all other errors")


answer = display_08()
print("Max ethnicity :", answer)

