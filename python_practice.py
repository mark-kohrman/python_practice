
# 1. Write a while loop to print the numbers 1 through 10.
i = 1
while i <= 10:
  print i
  i = i + 1

# # # 2. Write a while loop that prints the word "hello" 5 times.
i = 1
while i <= 5:
  print "hello"
  i += 1

# 3. Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".

while True:
    print("Please enter a word")
    word = input()
    if word == "stop":
        break


# 4. Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.
i = 0
while i <= 100:
  print (i)
  i += 1

# 5. Write a while loop that prints the number 9000 ten times.
number = 9000
i = 0
while i < 10:
    print (number)
    i += 1



# 6. Write a while loop that asks the user to enter a number and will run forever until the user enters a number greater than 10.
while True:
    print("Please enter a number")
    x = int(input())
    if x > 10:
        break


# 7. Write a while loop that prints the numbers 50 to 70.
x = 50
while x < 71:
    print(x)
    x +=1

# 8. Write a while loop that prints the phrase "Around the world" 144 times.

i  = 1
while i < 145:
    print("Around the world")
    print(i)
    i += 1

# 9. Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.
while True:
    print("Please enter a word")
    word = input()
    if len(word) > 5:
        break  



# 10. Write a while loop that prints the even numbers from 2 to 40.
x = 2

while x < 41:
    print(x)
    x += 2



# SOLUTIONS: https://gist.github.com/peterxjang/c4ec0e0f8f6e123d65ada9bf3100068b