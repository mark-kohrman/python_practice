# Write code that converts converts and prints out four different temperatures in Fahrenheit to Celsius. (Recall the formula for this conversion is (x - 32) * 0.5556, where x is the degrees in Fahrenheit).

# def fahrenheit_to_celsius(temperature):
#   temperature = (temperature - 32) * 0.5556
#   print(temperature)


# fahrenheit_to_celsius(29)

# When you run the code below, it should print lyrics. However, right now if you run the code, it doesn't print anything. Add the appropriate line of code to make the code run properly.


# def print_lyrics():
#    print("Now this is a story all about how")
#    print("My life got flipped turned upside down")
#    print("And I'd like to take a minute, just sit right there")
#    print("I'll tell you how I became the prince of a town called Bel-Air")

# print_lyrics()


# Create a function that accepts three numbers as inputs, and returns the product of all three numbers. So, if the three inputs were 2, 4, and 6, the output should be 48, which is 2 * 4 * 6.

# def product(number1, number2, number3):
#    print(number1 * number2 * number3)

# product(4, 2, 9)
#########################
# Write a function called select_less_than_five that takes in an array of numbers and returns a new array containing only the numbers less than 5. Then run the function with an input of [10, 3, 4, 55, 32, 6, 1] and print the output. The result should be:

# def select_less_than_five(array):
#    i = 0
#    lesser_array = []
#    while i < len(array):
#       if array[i] < 5:
#          print(array[i])
#          lesser_array.append(array[i])
#       i += 1
#    print(lesser_array)
      

# select_less_than_five([-3, 44, 2, 1, -6, 55, 9, -1])
###################
# WRITE: Write a function called say_hello that takes in a number, then prints out "Hello!" that many times.

# def say_hello(integer):
#    i = 0
#    while i < integer:
#       print('hello!')
#       i += 1

# say_hello(10)

##########
# DEBUG: Fix the errors in the code below.
# def double(input_number):
#    print(input_number * 2)

# double(3)
# double("four")
# double(5)
# double(6)
# double(8)
# double(9)

############

# Create a program that when you run it, prints the following:

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# BLASTOFF!

# countdown = 10
# while countdown > 0:
#    print(countdown)
#    countdown -= 1

# print("BLASTOFF!")


# Why waste your money on a human fortune teller when a computer can tell you your fortune for the same price?

# Exercise:

    
# Create a fortune teller which tells the user a fortune based on the user's favorite number. Give at least 3 possible outcomes. So along these lines, for example: If the user's favorite number is below 50, give fortune X. If the user's favorite number is between 50 and 100, give fortune Y. If the user's favorite number is above 100, give fortune Z.

print("Enter your favorite number to get your fortune:")
number = int(input())

if number < 25:
   print("You will win the lottery pretty soon")
elif number > 24 and number < 100:
   print("You will have a normal life but won't win the lottery, which is fine because money doesn't buy happiness dude")
else:
   print("You will have a monkey as a pet")



