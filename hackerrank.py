
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# def is_leap(year):
#     leap = False
#     if(year % 4 == 0):
#       leap = True
    
#     if(year % 4 == 0 and year % 100 == 0):
#       leap = False
    
#     if(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
#       leap = True
    
#     return leap

# print(is_leap(2400))

###############
# string = ""
# n = 3
# i = 1
# while i <= n:
#     string = string + str(i) 
#     i = int(i)
#     i+=1

# print(string)
########

# Start with this line of code:

# letter_groups = [["a", "b", "z"], ["c", "d"], ["e", "f"], ["g", "h", "i", "j"]]
# It's a two dimensional array (yay!).

# Write code that will take each of those letters and put them into a brand new one dimensional array. So the resulting array should be:

# ["a", "b", "z", "c", "d", "e", "f", "g", "h", "i", "j"]
# Your last line of code should use the p command (e.g. p new_array) to make sure that your new array looks right.


# list1 = [["a", "b", "z"], ["c", "d"], ["e", "f"], ["g", "h", "i", "j"]]

# list2 = []
# i = 0
# while i < len(list1):
#   i_2 = 0
#   while i_2 < len(list1[i]):   
#     list2.append(list1[i][i_2])
    
#     i_2 += 1
#   i += 1

# print(list2)