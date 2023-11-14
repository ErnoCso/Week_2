# Task 5

# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "le over"
# group.

lab_group = 24
students = [113, 175, 12]
print()  # it's not important, I just don't like it when the text runs together.
# I like to make the beginning of the program clearly visible, i.e. separate it.

for i in students:

    if (i // lab_group) == 0:
        print(f"In the case of {i} students a 'le over' group of {i % lab_group} students is required.")
    if (i // lab_group) != 0 and (i % lab_group) != 0:
        print(f"In the case of {i} students, {i // lab_group} full groups and one extra 'le over' group"
              f" will be needed for the remaining {i % lab_group} students.")
    if (i // lab_group) != 0 and (i % lab_group) == 0:
        print(f"In the case of {i} students, {i // lab_group} full group(s) will be needed.")

# Output

# In the case of 113 students, 4 full groups and one extra 'le over' group will be needed for the remaining 17 students.
# In the case of 175 students, 7 full groups and one extra 'le over' group will be needed for the remaining 7 students.
# In the case of 12 students a 'le over' group of 12 students is required.
