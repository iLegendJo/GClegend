def display_q03(lines):
    max_value = 0
    max_name = ""
    ethnicity = ""
    for line in lines:
        name = line[3]
        count = int(line[4])
        if count > max_value:
                max_value = count # contains the highest value when found check to see if higher than previous count
                max_name = name # associate max value with the name.
                ethnicity = line[2]
    return {"name":max_name,"count":max_value,"ethnicity":ethnicity}


with open("Popular_Baby_Names.csv", "r") as file_object:
    next(file_object)

    lines = [line.strip().split(",") for line in file_object if
             line.strip().split(",")[0] == '2014' and line.strip().split(",")[3] == "Eric" and line.strip().split(",")[1] == "MALE"]

    male_display = display_q03(lines )
    print(male_display)
