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
# Write a program that starts with an array of strings, then prints out each string on separate lines (using a while loop).

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


# DEBUG: The following code starts with an array and creates a new array with only the small numbers.
# input_numbers = [3, 2, 10, 4, 23, 9]
# new_numbers = []
# index = 0
# while index < len(input_numbers):
#   if input_numbers[index] < 10:
#     new_numbers.append(input_numbers[index])

#   index = index + 1

# print(new_numbers)

# 1. Create an array to store 3 words. Then add two more words to the array and print the array on one line.
# a = ["hey", "ho", "lets"]
# a.append("go")
# a.append("hey")

# print(a)

# # 2. Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.
# a = ["m", "n", "a", "p"]
# a[1] = 4
# print(a)
# 3. Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.
# numbers = [45, 12, 99, 123, 985]
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1


# # 4. Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.
# numbers = [4]
# numbers.extend([43, 12, 2])
# print(numbers)
# 5. Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.
# strings = ["hello", "slim", "shady"]
# strings[2] = strings[2].upper()
# print(strings)
# # 6. Create an array to store 3 names. Then print out each name on separate lines with a while loop.
# names = ["joe", "john", "alana"]
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1
# 7. Create an array to store 2 strings. Then add one string to the array and print the array on one line.
# array = ["make", "money"]
# array.append("buddy")
# print(array)
# # 8. Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.
# array = [12, 42, 123, 90, 3]
# array[0] = array[0] * 10
# print(array)
# 9. Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.
# numbers = [3, 99]
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1
# # 10. Create an array to store names of 3 different countries. Then add one more country and print the array one line.
# countries = ["Senegal", "Canada", "Japan"]
# countries.append("Vietnam")
# print(countries)

# SOLUTIONS: https://gist.github.com/peterxjang/7095a2b19e1da2cc18d4a0dcd66cb8f1

#  1. Start with an array of numbers and create a new array with each number times 3.
#     For example, [1, 2, 3] becomes [3, 6, 9].
numbers = [1, 2, 3]
new_array = []
for number in numbers:
    new_array.append(number * 3)

print(new_array)

#  2. Start with an array of strings and create a new array with each string upcased.
#     For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

strings = ["hello", "goodbye"]
capitalize = []
for string in strings:
    capitalize.append(string.upper())

print(capitalize)

#  3. Start with an array of hashes and create a new array of string values from each hash's :name key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].
peeps = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
names = []
for peep in peeps:
    names.append(peep["name"])

print(names)
#  4. Start with an array of numbers and create a new array with each number plus 7.
#     For example, [1, 2, 3] becomes [8, 9, 10].
numbs = [1, 2, 3]
new_numbs = []
for numb in numbs:
    new_numbs.append(numb + 7)

print(new_numbs)

#  5. Start with an array of strings and create a new array with each string's length.
#     For example, ["hello", "goodbye"] becomes [5, 7].
stringys = ["hello0000000", "goodbye"]
lengths = []
for stringy in stringys:
    lengths.append(len(stringy))

print(lengths)
#  6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].
persons = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages = []
for person in persons:
    ages.append(person["age"])

print(ages)

#  7. Start with an array of numbers and create a new array with each number divided by 2.
#     For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].
integers = [34, 98, 45]
divided = []
for integer in integers:
    divided.append(integer/2)

print(divided)
#  8. Start with an array of strings and create a new array with each string's first letter only.
#     For example, ["hello", "goodbye"] becomes ["h", "g"].
stringos = ["hello", "goodbye"]
first_letters = []
for stringo in stringos:
    first_letters.append(stringo[0])

print(first_letters)
# 9.  Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].
humans = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages_multiplied = []
for human in humans:
    ages_multiplied.append(human["age"] * 2)

print(ages_multiplied)

# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].
integers = [2, 88, 99]
string_ints = []
for integer in integers:
    string_ints.append(str(integer))

print(string_ints)

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/b9ac4390aad2301a2238efc95c904f3d
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/66598fd7cdbc67fe663624e217cebbaf
# SOLUTIONS (using .map shortcut): https://gist.github.com/peterxjang/23a8f8a51601e4288ba3a8aa6d1f1c98
