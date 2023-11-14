#!/usr/bin/env python 3

# Task 4

# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.

sweets = int(input("Please enter how many sweets there are in total: "))
pupils = int(input("Please enter number of pupils: "))
if sweets < pupils:
    print("You can't distribute the sweets fairly, because there are fewer sweets than there are students.")
elif sweets % pupils == 0 and sweets // pupils == 1:
    print(f"Each student gets exactly {sweets // pupils} sweet, no no remains.")
elif sweets % pupils == 0:
    print(f"Each student gets exactly {sweets // pupils} sweets, no remains.")
elif sweets // pupils == 1:
    print(f"Each pupil gets {sweets // pupils} sweet and has {sweets % pupils} left over ")
else:
    print(f"Each pupil gets {sweets // pupils} sweets and has {sweets % pupils} left over ")

# Output:

# Geoffrey Boycott:
#
#     Matches: 609
#     Batted: 1014
#     Times not out: 162
#     Runs scored: 48426
#     Boycott's batting average: 56.84

