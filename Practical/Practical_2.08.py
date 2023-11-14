# Task 8

# Input the following code, when asked to type your age input a numeric value such as 20.
# Does this program work? If not, why?
# age = input("Enter your age ")
# print("in one year your age will be", age + 1)

age = input("Enter your age ")
print("in one year your age will be", age + 1)

# Output:
#
# Enter your age 12
# Traceback (most recent call last):
#   File "C:\Users\Relaxatio\OneDrive - Leeds Beckett University\Python\Week2\Practical\Practical_7.08.py", line 9, in <module>
#     print("in one year your age will be", age + 1)
#                                           ~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# The code doesn't work because the program treats the "age" variable as a string,
# since we didn't specify anywhere that it should be treated as an integer.