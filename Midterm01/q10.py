# read  original csv file.
# filter the data to grab females and males
# Create 2 new csv files


def question_ten_test(gender):
    try:
        gender = gender.upper()
        with open("Popular_Baby_Names.csv", 'r') as file_object:
            next(file_object)
            lines = [line.strip().split(",") for line in file_object if line.strip().split(",")[1] == gender]

            with open(gender.lower() + "_names.csv", "w") as f:
                for line in lines:
                    f.write(line[0]+","+line[3]+","+line[4] + "," + line[5] + "\n")
                    # f.write(line)
                    # print(line)

            # f.close()
    #         I believe the f.close is not needed since the with is already dealing with closing the file.
    except FileNotFoundError:
        print("The file not found - please review file name")
    except:
        print("all other errors")

question_ten_test("female")
question_ten_test("male")
# print(female)
