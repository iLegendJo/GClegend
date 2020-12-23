def get_name_by_ethnicity(year,ethnicity,gender,rank):
    try:

        with open("Popular_Baby_Names.csv", "r")as file_object:
            next(file_object)

            lines = [line.strip().split(",") for line in file_object]
            line_two =[line for line in lines if line[0] == year and line[2].find(ethnicity) > -1 and line[1] == gender
                       and line[5] == rank]
            return_value = '""'
            if len(line_two) > 0:
                return_value = line_two[0][3]

            return return_value

    except FileNotFoundError:
        print("The file not found")
    except:
        print("all other errors")


input_year = input("Please enter year:")
input_ethnicity = input("Please enter ethnicity:").upper()
input_gender = input("Please enter gender: ").upper()
input_rank = input("Please enter rank: ")

answer = get_name_by_ethnicity(input_year, input_ethnicity, input_gender, input_rank)
print(answer)