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

numbers = [3, 4, 1, 2]
i = 0
while i < len(numbers):
  print(f"The number is {numbers[i]}.")
  i += 1

  #############

  # DEBUG Print out every number + 2
numbers = [4, 5, 2, 1]
index = 0
while index < len(numbers):
   print(numbers[index] + 2)
   index = index + 1



