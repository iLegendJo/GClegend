def display_07(year_entered, rank_entered):
    try:
        with open("Popular_Baby_Names.csv", "r") as file_object:
            next(file_object)

            lines = [line.strip().split(",") for line in file_object ]
            line_two = [line for line in lines if  line[0]== year_entered and line[5] == rank_entered]
        return line_two

    except FileNotFoundError:
        print("The file not found")
    except:
        print("all other errors")


year = input("Please enter year:" )
rank = input("Please enter rank: ")
answer = display_07(year, rank)
for result in answer:
    print(result[3], result[1],result[4])

if 0 == len(answer):
    print("No names found")
    # print(result)