names = input(f"Please enter your first, middle and last name.:")
namesplit = names.split()
finalname = ""

for name in namesplit:
    finalname += name[0] + ". "

print(f"this is final name: {finalname}")

