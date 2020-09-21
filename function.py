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

######################
# Why waste your money on a human fortune teller when a computer can tell you your fortune for the same price?

# Exercise:

    
# Create a fortune teller which tells the user a fortune based on the user's favorite number. Give at least 3 possible outcomes. So along these lines, for example: If the user's favorite number is below 50, give fortune X. If the user's favorite number is between 50 and 100, give fortune Y. If the user's favorite number is above 100, give fortune Z.

# print("Enter your favorite number to get your fortune:")
# number = int(input())

# if number < 25:
#    print("You will win the lottery pretty soon")
# elif number > 24 and number < 100:
#    print("You will have a normal life but won't win the lottery, which is fine because money doesn't buy happiness dude")
# else:
#    print("You will have a monkey as a pet")

################## MAD LIBS

# Write a program that asks the user for 5 words and creates a story out of it. For example, your program will have some sort of story template like this:

# ____name____ went to the store and bought a ___noun___. Then, the ____adjective____ ____noun____ yelled, "Quick! Go ____verb____ the police!"

# In the above example, the program will ask the user for a name, a noun, an adjective, another noun, and a verb. After the user enters those words, the program will print out the completed story.

# For this exercise, use interpolation

# print("Enter a noun to get started with your new story: ")
# noun1 = input()
# print("Enter a verb: ")
# verb1 = input()
# print("Enter an adjective")
# adjective1 = input()
# print("Enter another noun please: ")
# noun2 = input()
# print("Enter a verb to complete the story and print it: ")
# verb2 = input()

# print(f"I went to the store and saw a big {noun1}.  I {verb1} because it was so {adjective1} yet calming in a way.  Luckily I saw my {noun2}.  I knew then it would help if I {verb2} a taco.")

#########

# Create program that multiplies by 2 until 100,000. That is, the program should print out:

# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# # etc... until you get above 100,000.
# number = 1
# while number < 100001:
#    print(number)
#    number *= 2
##########################



# Exercise:

    
# Create a program that asks the user to enter 5 numbers. Then, tell the user the mean average of all the numbers.

# The mean average is defined as the sum of all the numbers divided by the count of how many numbers there are. For example, if the user enters:

# 11, 7, 30, 22, 55

# the average will be 25. This is because 11 + 7 + 30 + 22 + 55 = 125, and 125 / 5 (the amount of numbers in the list) = 25.

# Note: If you run the code p 9 / 2, it prints 4 even though the result should be 4.5. This is because when dividing integers in Ruby, the result will be an integer. If you want an answer with decimals, at least one of the numbers should be a decimal. If you run the code p 9 / 2.to_f, it prints 4.5 as you would expect. This is because the .to_f converts the integer to a floating point number which contains decimals.

# i = 0
# sum = 0
# mean_list = []
# while i < 5:
#    print("Please enter a number and you will get the average of 5 numbers:")
#    number = int(input())
#    mean_list.append(number)
#    sum += number
#    i += 1

# mean = sum / len(mean_list)
# print(f"The mean of the numbers you entered is {mean}")

########################

# Create a program that asks the user to enter 5 numbers. Then, tell the user the median number. The definition of a median number is found here.

# Bonus: Make your code work with any size array. This is harder than the problem above, since the definition of median is different when there are an even or odd amount of numbers. If you want, you can use the integer .even? and .odd? methods to help solve this problem.

# i = 0
# median_list = []
# while i < 5: 
#    print("Please enter 5 numbers to get the median:")
#    number = int(input())
#    median_list.append(number)
#    i += 1

# median_list.sort()
# print(f"The median of the  numbers is {median_list[2]}.")

# i = 0
# median_list = []
# while True: 
#    print("Please numbers to get a median and type 'done' to get the median:")
#    number = input()
#    if number == "done":
#       break
   
#    median_list.append(int(number))


# median_list.sort()
# middle = (len(median_list) / 2)
# if(len(median_list) % 2 != 0 ):
   
#    # print(median)
#    index1 = ((len(median) / 2) - 2)
#    print(index1)

# print(type(median_list[1]))
# print(f"The median of the  numbers is {median_list[2]}.")

#############

# Have a user enter 5 numbers, and have it so that the program tells you the highest of all those numbers. Catch: Don't use the max method (which does that for you). Use a loop instead.
i = 0
numbers = []
while i < 5:
   print("please enter a #:")
   number = int(input())
   numbers.append(number)
   i += 1

max = numbers[0]
i_2 = 0
while i_2 < len(numbers):
   if numbers[i_2] > max:
      max = numbers[i_2]
   i_2 += 1

print(f"Your highest number is {max}.")




