# Write a program that asks the user to type in a word, and the program outputs the word in two different ways: A) It displays the string in reverse B) It displays the string in all capital letters.

# print("Please enter a word:")
# word = input()
# print(word[::-1])
# print(word.upper())

# 3 string documentation methods.  

# print("Hello".count("l"))

# print("Lemon".endswith("a"))

# print("JOSEPHINE".capitalize())
#######################
# Write a program that asks the user for their name. If the user enters their name in all capital letters, the program will print “NICE TO MEET YOU!”. Otherwise, the program will print “I CAN’T HEAR YOU!”. (This problem is a little tricky!)

# print("Please enter your name:")
# name = input()

# if name == name.upper():
#   print("NICE TO MEET YOU!")
# else:
#   print("I CAN'T HEAR YOU!")

####################
# Write a program that asks the user for their name and age, then outputs a greeting message and how old they'll be in 10 years. For example, if Alejandra enters her name and age of 28, the program will output "Welcome Alejandra! In 10 years, you will be 38!"
# print("please enter your name then age")
# name = input()
# age = int(input()) + 10
# print(name)
# print(age)

# print(f"Welcome {name}! In 10 years, you will be {age}!")


# WRITE: Create a program that says "I'm thinking of a number between 1 and 100", and asks the user to guess which number the computer is thinking of. The correct answer is 33. So, if the user guesses 33, the computer should say, “You win!”. If the number is less than 33, it should say, “Too low.” If the number is greater than 33, it should say, “Too high.”

# print("I'm thinking of a number between 1 and 100, please guess which number:")
# number = int(input())

# if number == 33:
#   print("You win!!!")
# elif number < 33:
#   print("Too low.")
# else:
#   print("Too high.")