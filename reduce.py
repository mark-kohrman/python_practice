from functools import reduce

#  1. Start with an array of numbers and compute the sum of all the numbers.
#     For example, [5, 10, 8, 3] becomes 26.

array = [5, 10, 8, 3]
sum = reduce((lambda a, b: a+b), array)
print(sum)
#  2. Start with an array of strings and combine them all into a single string.
#     For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".
sports = ["volleyball", "basketball", "badminton"]
combined_sports = reduce((lambda a, b: a + b), sports)
print(combined_sports)
#  3. Start with an array of hashes and compute the sum of the prices (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.
items = [{"name": "chair", "price": 100}, {
    "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
sum_price = 0
i = 0
while i < len(items):
    sum_price += items[i]["price"]
    i += 1

print(sum_price)
#  4. Start with an array of numbers and compute the the minumum number.
#     For example, [5, 10, 8, 3, 9] becomes 3.
numbers = [5, 10, -8, 3, 9]
minmum = numbers[0]

for number in numbers:
    if number < minmum:
        minmum = number

print(minmum)

#  5. Start with an array of strings and compute the total length of all the strings.
#     For example, ["volleyball", "basketball", "badminton"] becomes 29.
strings = ["volleyball", "basketball", "badminton"]
total_string_length = 0
i = 0
while i < len(strings):
    total_string_length += len(strings[i])
    i += 1

print(total_string_length)


#  6. Start with an array of hashes and find the hash with the lowest price (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.
products = [{"name": "chair", "price": 100}, {
    "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
minimum_price = products[0]
# print(minimum_price)

for product in products:
    if product["price"] < minimum_price["price"]:
        minimum_price = product

print(minimum_price)

# print(minimum_price)
#  7. Start with an array of numbers and compute product of all the numbers.
#     For example, [5, 10, 8, 3] becomes 1200.

#  8. Start with an array of strings and combine them all into a single string, separated by dashes.
#     For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

#  9. Start with an array of hashes and find the hash with the shortest name (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

# 10. Start with an array of numbers and compute the maximum number.
#     For example, [5, 10, 8, 3] becomes 10.


# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/376c8931a48549889eb3c9bc091e9f43
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/379c9945774f51027750c59d6e4395df
# SOLUTIONS (using .reduce shortcut): https://gist.github.com/peterxjang/b69183e2d555964ce3936893f423ef35
