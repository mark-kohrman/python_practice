#  1. Start with an array of numbers and create a new array with only the numbers less than 20.
#     For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].
numbers = [2, 32, 80, 18, 12, 3]
less_than = []
i = 0
while i < len(numbers):
    if numbers[i] < 20:
        less_than.append(numbers[i])
    i += 1

print(less_than)
#  2. Start with an array of strings and create a new array with only the strings that start with the letter "w".
#     For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].
words = ["winner", "winner", "chicken", "dinner", "wool"]
w_words = []
for word in words:
    if word[0] == "w":
        w_words.append(word)

print(w_words)

#  3. Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].
items = [{"name": "chair", "price": 100}, {
    "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
expensive_items = []
i = 0
while i < len(items):
    if items[i]["price"] > 5:
        expensive_items.append(items[0])

    i += 1

print(expensive_items)

#  4. Start with an array of numbers and create a new array with only the even numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].
integers = [2, 4, 5, 1, 8, 9, 7]
even_ints = []
for integer in integers:
    if integer % 2 == 0:
        even_ints.append(integer)

print(even_ints)

#  5. Start with an array of strings and create a new array with only the strings shorter than 4 letters.
#     For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].
words = ["a", "man", "a", "plan", "a", "canal", "panama", "yo", "leaves"]
short_words = []
i = 0
while i < len(words):
    if len(words[i]) < 4:
        short_words.append(words[i])
    i += 1

print(short_words)
#  6. Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].
supplies = [{"name": "chair", "price": 100}, {
    "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
short_supplies = []
for supply in supplies:
    if len(supply["name"]) < 6:
        short_supplies.append(supply)

print(short_supplies)

#  7. Start with an array of numbers and create a new array with only the numbers less than 10.
#     For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].
numbs = [8, 23, 0, 44, 1980, 3]
low_numbs = []
i = 0

while i < len(numbs):
    if numbs[i] < 10:
        low_numbs.append(numbs[i])
    i += 1

print(low_numbs)

#  8. Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
#     For example, ["big", "little", "good", "bad"] becomes ["little", "good"].
words = ["big", "little", "good", "bad"]
not_b_words = []

for word in words:
    if word[0] != "b":
        not_b_words.append(word)

print(not_b_words)
#  9. Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].
items = [{"name": "chair", "price": 100}, {
    "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
cheap_items = []
i = 0

while i < len(items):
    if items[i]["price"] < 10:
        cheap_items.append(items[i])
    i += 1

print(cheap_items)
# 10. Start with an array of numbers and create a new array with only the odd numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].
numbers = [2, 4, 5, 1, 8, 9, 7]
odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/7de16ed43ea506e98df3fa15074b84f8
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/a702894841c7018ed8c127b647ae21f8
# SOLUTIONS (using .select shortcut): https://gist.github.com/peterxjang/b8c8fb8b77b2cae7bb9cc62a3a434761
