students = int(input("Please enter how many students there are in total: "))
groups = int(input("Please enter the required group size: "))
if students % groups == 1:
    print(f"There will be {students // groups} groups with {students % groups} student left over")
elif students % groups == 0 and students / groups == 1:
    print(f"There will be {students // groups} group")
elif students % groups == 0:
    print(f"There will be {students // groups} groups")
else:
    print(f"There will be {students//groups} groups with {students%groups} students left over")

