# Task 10
#
# comment = 'I would have "thought" you knew better!'
# Try writing the above assignment statement but only use double quotes
# instead of single quotes as the string delimiter. What is the result?

comment = "I would have \"thought\" you knew better!"
print(comment)

# Output:
####################################################################################################################
# If I just replace any single quotes with double quotes, I get an error:
#
# comment = "I would have "thought" you knew better!"
# print(comment)
#  File "C:\Users\Relaxatio\OneDrive - Leeds Beckett University\Python\Week2\Practical\Practical_7.10.py", line 7
#    comment = "I would have "thought" you knew better!"
#                             ^^^^^^^
# SyntaxError: invalid syntax
###################################################################################################################
# But if I use backslashes in the middle, I can avoid this error:
#
# comment = "I would have \"thought\" you knew better!"
# print(comment)
#
# I would have "thought" you knew better!
##################################################################################################################