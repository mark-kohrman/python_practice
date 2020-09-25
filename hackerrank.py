
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

########################
# string = "Joseph MiXon"
# new_string = ""
# i = 0
# while i < len(string):
#   if string[i].islower():
#     new_string = new_string + string[i].upper()
#   else:
#     new_string = new_string + string[i].lower()
#   i += 1

# print(new_string)

#########

# n = int(raw_input())
# student_marks = {}
# for _ in range(n):
#     line = raw_input().split()
#     name, scores = line[0], line[1:]
#     scores = map(float, scores)
#     student_marks[name] = scores
# query_name = raw_input()
#     student_marks[query_name] = (scores[0] + scores[1] + scores[2]) / 3
#     print()

##############
# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# def weird_or_not(n):
#   if n % 2 != 0:
#     print("Weird")
#   elif n % 2 == 0 and n >= 2 and n <= 5:
#     print("Not Weird")
#   elif n % 2 == 0 and n >= 6 and n <= 20:
#     print("Weird")
#   else:
#     print("Not Weird")


# weird_or_not(31)
a = "Mark"
b = "Kohrman"

print(f"Hello {a} {b}! You just delved into python.")
