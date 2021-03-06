# #  1. Convert an array of arrays into a hash.
# #     For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.
# arrays = [[1, 3], [8, 9], [2, 16]]
# dictionary = {}
# i = 0
# while i < len(arrays):
#     i_2 = 0
#     while i_2 < len(arrays[i]):
#         dictionary[arrays[i][i_2]] = arrays[i][i_2 + 1]
#         i_2 += 2
#     i += 1

# print(dictionary)

# #  2. Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
# #     For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.
# items = [{"id": 1, "color": "blue", "price": 32},
#          {"id": 2, "color": "red", "price": 12}]
# item_hash = {}
# i = 0
# while i < len(items):
#     key = items[i]["id"]
#     value = items[i]
#     item_hash[key] = value
#     i += 1

# print(item_hash)

#  3. Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
# #     For example, "bookkeeper" becomes {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}.

# word = "bookkeeper"
# letters = {}
# i = 0
# while i < len(word):
#     key = word[i]
#     if letters[key] == None:
#         letters[key] = 0

#     letters[key] += 1
#     i += 1

# i_2 = 0
# while i_2 < len(word):
#     key = word[i_2]
#     if letters[key] == None:
#         letters[key] = 1
#     else:
#         letters[key] += 1
#     i_2 += 1

# print(letters)


#  4. Convert a hash into an array of arrays.
#     For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].

# stuff = {"chair": 100, "book": 14}
# items_list = []
# i = 0
# for key, value in stuff.items():
#     items_list.append([key, value])

# print(items_list)


#  5. Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
#     For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

#  6. Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
#     For example, ["do", "or", "do", "not"] becomes {"do" => 2, "or" => 1, "not" => 1}.

#  7. Convert a hash into a flat array containing all the hash’s keys and values.
#     For example, {"a" => 1, "b" => 2, "c" => 3, "d" => 4} becomes ["a", 1, "b", 2, "c", 3, "d", 4].
# letters = {"a": 1, "b": 2, "c": 3, "d": 4}
# letter_list = []
# for key, value in letters.items():
#     letter_list.append(key)
#     letter_list.append(value)

# print(letter_list)
#  8. Combine data from a hash with names and prices and an array of hashes with names, colors, and weights to make a new hash.
#     For example, {"chair" => 75, "book" => 15} and [{name: "chair", color: "red", weight: 10}, {name: "book", color: "black", weight: 1}] becomes {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}.

hash1 = {"chair": 75, "book": 15}
array = [{"name": "chair", "color": "red", "weight": 10},
         {"name": "book", "color": "black", "weight": 1}]
combined_hash = {}

#  9. Convert an array of hashes into a hash of arrays, using the author as keys and the titles as values.
#     For example, [{author: "Jeff Smith", title: "Bone"}, {author: "George Orwell", title: "1984"}, {author: "Jeff Smith", title: "RASL"}] becomes {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}.
books = [{"author": "Jeff Smith", "title": "Bone"}, {
    "author": "George Orwell", "title": "1984"}, {"author": "Jeff Smith", "title": "RASL"}]
book_dict = {}
book_list = []
i = 0
while i < len(books):
    book = books[i]
    key = book["author"]
    value = book["title"]
    book_dict[key] = None
    i += 1

i = 0
while i < len(books):
    book = books[i]
    key = book["author"]
    value = book["title"]
    if book_dict[key] == None:
        book_dict[key] = []
    book_dict[key].append(value)
    i += 1


print(book_dict)
# print(book_dict)
# hello = None
# dictionary = {}
# dictionary["key"] = None
# if hello is None:
#     print(dictionary)
# 10. Given a hash, create a new hash that has the keys and values switched.
#     For example, {"a" => 1, "b" => 2, "c" => 3} becomes {1 => "a", 2 => "b", 3 => "c"}.
letters = {"a": 1, "b": 2, "c": 3}
switched_letters = {}
for key, value in letters.items():
    switched_letters[value] = key

# print(switched_letters)


# SOLUTIONS: https://gist.github.com/peterxjang/216a7a6e8411ee5c05118e78022f2bc7
