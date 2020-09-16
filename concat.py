# Read the code and predict which lines will crash. Then run the code and remove the invalid lines one at a time, until only the valid code remains.

# print(9 + 3)
# print("9" + "3")
# print(9 - 3)
# print(9 * 3)
# print("9" * 3)
# print(9 * "3")
# print(9 / 3)

# ############2

# bob = "maria"     # 1
# maria = "bob"     # 2
# x = bob + maria   # 3
# print(x)          # 4
# x = "bob" + maria # 6
# print(x)           # 7


# # 1: bob is "maria"
# # 2: bob is "maria", maria is "bob"
# # 3: bob is "maria", maria is "bob", x is "maria" + "bob" 
# # 4: "
# # 6: bob is "maria", maria is "bob", x is "bob" + "bob"
# # 7: "

# #### Rewrite the code below to use string interpolation instead of concatenation.
# first_name = "Katherine"
# last_name = "Johnson"
# # puts first_name + " " + last_name + " was a NASA research mathematician."

# print(f"{first_name} {last_name} was a NASA research mathematician.")


# Write code that asks the user for their name, then asks for their favorite color, then prints out back to them their name and favorite color in a sentence.

# print("Please enter your name")
# user_name = input()
# print("Please enter your favorite color")
# favorite_color = input()

# print(f"Your name is {user_name} and your favorite color is {favorite_color}.")


# Write code that asks the user for their name, then asks for their favorite color, then prints out back to them their name and favorite color in a sentence.

############5

# Create a program in which the user is asked for their name. After the user enters their name, the computer should print “Cool!”, unless their name is “Qwerty” - in which case, the computer should print “Really?”

# print("Please enter your name: ")
# user_name = input()

# if user_name == "Qwerty":
#   print("Really?")
# else:
#   print("Cool!")
###############################
# WRITE: Write code to ask the user for a day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). If the user enters Monday, print out the message "Sounds like someone has a case of the Mondays!". For any other weekday, print out the message "Time to make the Donuts!". For any weekend day, print out the message "It's the weekend. Enjoy it.". If the user did not enter a valid day, print out the message "That does not compute. Try again!"

print("Please enter a day of the week:")
day = input()

if day == "Monday":
  print("Sounds like someone has a case of the Mondays")
elif day == "Saturday" or day == "Sunday":
  print("It's the weekend.  Enjoy it")
elif day == "Tuesday" or day =="Wednesday" or day =="Thursday" or day == "Friday":
  print("Time to make donuts!")
else: 
  print("That does not compute.  Try again!")



###################DEBUG

print("Welcome to The Matrix. Do you want to take the red pill or the blue pill?")

pill = input()

if pill == "red":
  print("You took the red pill.")
if pill == "blue":
  print("You took the blue pill.")



