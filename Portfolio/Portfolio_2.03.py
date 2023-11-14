#!/usr/bin/env python 3

# Task 2

# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be le over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.



def main():
    ans1 = ["Yes", "yes", "YES", "Y", "y", "Yeah", "YEAH", "yeah"]
    ans2 = ["No", "no", "NO", "N", "n", "Nope", "NOPE", "nope"]
    students = int(input("Please enter how many students there are in total: "))
    groups = int(input("Please enter the required group size: "))
    if students % groups == 1:
        print(f"There will be {students // groups} full groups with {groups} students "
              f"and an extra 'leftover' group consisting of only {students % groups} student.")
    elif students % groups == 0 and students / groups == 1:
        print(f"There will be {students // groups} group with {groups} students.")
    elif students % groups == 0:
        print(f"There will be {students // groups} full groups with {groups} students per group.")
    elif students//groups == 0:
        print(f"There will be only one incomplete group consisting of {students} students. ")
    elif students % groups == 1 and students / groups == 1:
        print(f"There will be {students // groups} full groups with {groups} students "
              f"and an extra 'leftover' group consisting of only {students % groups} students.")
    else:
        print(f"There will be {students // groups} full groups with {groups} student per group "
              f"and an extra 'leftover' group consisting of {students % groups} students.")

    def question():
        q = input("Would you like to enter another number? Y/N ")
        if q in ans1:
            main()
        if q in ans2:
            print("Goodbye!")
            exit()
        else:
            print("Invalid data, please try again ")
            question()

    question()


if __name__ == "__main__":

    main()

# Output:
#
# Please enter how many students there are in total: 48
# Please enter the required group size: 24
# There will be 2 full groups with 24 students per group.
# Would you like to enter another number? Y/N y
# Please enter how many students there are in total: 14
# Please enter the required group size: 24
# There will be only one incomplete group consisting of 14 students.
# Would you like to enter another number? Y/N y
# Please enter how many students there are in total: 14
# Please enter the required group size: 14
# There will be 1 group with 14 students.
# Would you like to enter another number? Y/N y
# Please enter how many students there are in total: 113
# Please enter the required group size: 22
# There will be 5 full groups with 22 student per group and an extra 'leftover' group consisting of 3 students.
# Would you like to enter another number? Y/N y
# Please enter how many students there are in total: 144
# Please enter the required group size: 24
# There will be 6 full groups with 24 students per group.
# Would you like to enter another number? Y/N n
# Goodbye!