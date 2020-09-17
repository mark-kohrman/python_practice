# Write a program that asks the user to enter a word, and the program will output the letters of that word in random order. (For example, "cat" may output "atc" or "tac" or "act" etc.) To accomplish this, investigate the following methods:
# The string's "split" method
# The array's "shuffle" method
# The array's "join" method

# import random
# print("Please enter a word")
# word = input()
# shuffled = list(word)
# random.shuffle(shuffled)
# shuffled = ''.join(shuffled)

# print(shuffled)

# Create a program that asks a user to enter four different words, one at a time. Then, the computer will ask the user to choose a number between 0 and 3. The computer will then display the word corresponding to the correct number. For example, assume the user typed in the words: "ghost", "umbrella", "candy", and "pepperoni" - in that order. The user is then prompted to choose a number. If the user chooses the number 2, the computer displays the third word, which in this example is "candy".

# array = []

# for word in range(0, 4):
#   print("Please enter a word:")
#   word = input()
#   array.append(word)

# print(array)
# print("Please enter a number from 0-3:")
# number = int(input())
# print(array[number])


#################
#Write a program that starts with an array of strings, then prints out each string on separate lines (using a while loop).

# religions = ["Buddhism", "Christianity", "Judaism", "Islam"]
# i = 0
# while i < len(religions):
#   print(religions[i])
#   i += 1
############################

# Write a program that starts with an array of numbers, then prints out each number times 3 (using a while loop). For example, if your starting array is [2, 4, 1, 5], the output should be

# numbers = [4, 45, 12]
# i = 0
# while i < len(numbers):
#   print(numbers[i] * 3)
#   i += 1

################
# WRITE: Start with this code:
# numbers = [3, 4, 1, 2]
# Write a while loop to print out each number in a sentence, one line at a time. The output should look like the following:

# numbers = [3, 4, 1, 2]
# i = 0
# while i < len(numbers):
#   print(f"The number is {numbers[i]}.")
#   i += 1

#   #############

#   # DEBUG Print out every number + 2
# numbers = [4, 5, 2, 1]
# index = 0
# while index < len(numbers):
#    print(numbers[index] + 2)
#    index = index + 1

# Write a program that starts with an array of numbers, then prints out a new array using a p statement with every number times ten. For example, if your starting array is [2, 4, 1, 5], the output should be

# numbers = [2, 4, 1, 5]
# times_ten = []
# i = 0

# while i < len(numbers):
#   times_ten.append(numbers[i] * 10)
#   i += 1

# print(times_ten)

###################
# Write code that takes the array [3, 123, 433, -77, 56, 200, 99, 101, 6] and prints out on each line only the numbers that are greater than 100. Your output should be this:

# numbers = [3, 123, 433, -77, 56, 200, 199, 101, 6] 

# i = 0
# while i < len(numbers):
#   if numbers[i] > 100:
#     print(numbers[i])

#   i += 1
#####################

# Write code that takes the array ["cat", "remove", "list", "change"] and prints out a brand new array on a single line with words with 4 or fewer letters. Your output should be this:

# words = ["cat", "remove", "list", "change"]
# i = 0

# while i < len(words):
#   if len(words[i]) <= 4:
#     print(words[i])
#   i += 1

##########
# Write code that takes the array [8, 3, 10, 4] and prints out the product of all the numbers using a loop. Your output should be this:

# numbers = [8, 3, 10, 4]
# i = 0
# product = 1

# while i < len(numbers):
#   product = product * numbers[i]
#   i += 1


# print(product)

############
# Start with the array coordinates = [[3, 2], [2, 10], [4, 0]] Print out the third sub-array, then print out the second item of that sub-array. The result should be:

# numbers = [[3, 2], [2, 10], [4, 0]] 
# print(numbers[2])
# print(numbers[2][1])

#################
# WRITE: Start with the array [5, 10, 15, 4, 9], then use a while loop to create a new array that has all those values plus 7, then print the new array. The output should be:

# numbers = [5, 10, 15, 4, 9]
# plus_seven = []
# i = 0

# while i < len(numbers):
#   plus_seven.append(numbers[i] + 7)
#   i += 1

# print(plus_seven)


####DEBUG: The following code starts with an array and creates a new array with only the small numbers.
# input_numbers = [3, 2, 10, 4, 23, 9]
# new_numbers = []
# index = 0
# while index < len(input_numbers):
#   if input_numbers[index] < 10:
#     new_numbers.append(input_numbers[index])
  
#   index = index + 1

# print(new_numbers)


