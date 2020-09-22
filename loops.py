# Write a loop to generate the following output:
# I know you are
# But what am I?
# I know you are
# But what am I?
# I know you are
# But what am I?
# I know you are
# But what am I?
###Answer
# for x in range(0, 4):
#   print("I know you are")
#   print("But what am I?")


#########

# WRITE: Write a program using a loop that prints out the entire exact lyrics of the famous song "99 Bottles of Beer on the Wall". You can find the lyrics here.
####ANSWER
# bottles = 100
# while bottles > 1:
#   bottles -=1
#   if bottles > 2:
#     print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
#     print(f"Take one down pass it around {bottles - 1} bottles of beer on the wall")
#   elif bottles == 2:
#     print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
#     print(f"Take one down pass it around {bottles - 1} bottle of beer on the wall")
#   else:
#     print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
#     print(f"Take one down pass it around no more bottles of beer on the wall")

#     print(f"No more bottles of beer on the wall, no more bottles of beer.")
#     print(f"Go to the store and buy some more, 99 bottles of beer on the wall")

# Write the code to print out all numbers from 200 to 300 with a for loop. Then write the code to print out all numbers from 200 to 300 with a while loop instead.

# for x in range(200, 301):
#   print(x)
# x = 200
# while x < 301:
#   print(x)
#   x += 1

# The following code will run 100 times, and each time it will ask the user for their name. The code will break early if the user’s name is Bob.

# 100.times do
#   puts "What is your name?"  
#   name = gets.chomp
#   if name == "Bob"
#     break
#   end
# end

# puts "Hi, Bob!"
# Rewrite the code using a while loop so the program will run *forever* unless the user enters a name of Bob.

# while True:
#   print("Please enter your name:")
#   name = input()
#   if name == "Bob":
#     break


# print("Hi Bob")

# ######The following code is supposed to print the numbers 1 to 10, but it currently doesn't work. Find the mistake and fix the code.
# for x in range(1, 11):
#   print(x)
#   x = x + 1


######
# WRITE: Use a .times loop to print the numbers 5, 10, 15, 20, etc., all the way up to 100. Then write code to produce the same result using a while loop instead.

# for x in range(5, 101, 5):
#   print(x)

# x = 5
# while x < 101:
#   print(x)
#   x += 5


# puts "This code should output the following sequence: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, BLASTOFF!"
# x = 10
# while x < 1
#   p x
#   x = x - 1
#   puts "BLASTOFF!"
# end

# x = 10
# while x > 0:
#   print(x)
#   x = x - 1

# print("BLASTOFF!")

#######################
  # It's an array of hashes that is used to represent data about different people. Use a loop within a loop to print out the list of everyone's hobbies in ALL CAPS. So the result should look like this:



# people = [
#   {
#     "first_name": "Robert",
#     "last_name": "Garcia", 
#     "hobbies": ["basketball", "chess", "phone tag"]
#    },
#    {
#     "first_name": "Molly",
#     "last_name": "Barker",
#     "hobbies": ["programming", "reading", "jogging"]
#    },
#    {
#     "first_name": "Kelly",
#     "last_name": "Miller",
#     "hobbies": ["cricket", "baking", "stamp collecting"]
#    }
# ]

# i = 0
# while i < len(people):
#   i_2 = 0
#   while i_2 < len(people[i]["hobbies"]):
#     print(people[i]["hobbies"][i_2].upper())
#     i_2 += 1
#   i += 1

############
#
# The rest of your program should create and print out an array that removes all duplicates from the original array.

# numbers = [4, 6, 1, 4, 2, 8, 3, 4, 1, 7]
# new_numbers = []

# numbers = sorted(numbers)
# frequencies = 0
# i = 0
# while i < len(numbers):
#   if numbers[i] != numbers[i - 1]:
#     new_numbers.append(numbers[i])
#   i += 1

# print(new_numbers)

#####################
# Fibonacci numbers are numbers that follow the pattern: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc.

# That is, each number is the sum of the two numbers that precede it.

# Write a program that prints out the first 100 fibonacci numbers. Use a loop!


# fibonacci = [0, 1]
# i = 1
# while i < 101:
#   new_fibo_number = fibonacci[i] + fibonacci[i - 1]
#   fibonacci.append(new_fibo_number)
#   print(new_fibo_number)
#   i += 1

################################

    
# Have the user enter 10 words, and allow for duplicate words. After the user is done, the program will tell the user which word was entered the most frequently.

# For example, if the user enters:

# apple, banana, orange, pear, apple, pear, apple, squash, apple, pear

# The program will say:

# apple was your most common word
# (That's because apple appeared in the user's list 4 times, more than any other word.)

# HINT: USE A HASH TO KEEP TRACK OF HOW MANY TIMES EACH WORD APPEARS IN THE LIST.

fruits = []
i_3 = 0
while i_3 < 11:
  print("Please enter a fruit until you are asked to stop:")
  fruit = input()
  fruits.append(fruit)
  i_3 += 1

print(fruits)

frequencies = {}
i = 0
while i < len(fruits):
  key = fruits[i]
  value = "nil"
  frequencies[key] = value
  i += 1

i_2 = 0
max = 0
while i_2 < len(fruits):
  key_2 = fruits[i_2]
  if frequencies[key_2] == "nil":
    frequencies[key_2] = 1
  else:
    frequencies[key_2] += 1
  
  if max < frequencies[key_2]:
    max = frequencies[key_2]
    max_fruit = key_2
  i_2 += 1


print(f"The most frequent word is {max_fruit}")

  





  
