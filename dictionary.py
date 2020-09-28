# # # Add populations to the city_populations hash for New York City {8.4 million) and San Francisco (800,000). The result should be, "title": "Murder Story Scary", "page_count": 900, "language": "Spanish"}
# print(book["author"])
# print(title("title"))
# print()


# # # city_populations = {"Chicago": 2700000}

# # # city_populations["New York City"] = 8400000
# # # city_populations["San Francisco"] = 800000


# # # print(city_populations)

# # ####################


# # # Assume you have the following code:
# # # drink1 = {"name": "Seltzer", "ingredients": ["water", "bubbles"]}
# # # drink2 = {"name": "Coca Cola", "ingredients": ["water", "bubbles", "sugar", "brown food coloring"]}
# # # drink3 = {"name": "water", "ingredients": ["hydrogen", "oxygen"]}
# # # # Write a line of code to print out the name for drink1. Then write a line of code to print out the ingredients for drink1. Then write a line of code to print out only the first ingredient for drink1. The final output should be:
# # # # "Seltzer"
# # # # ["water", "bubbles"]
# # # # "water"

# # # print(drink1["name"])
# # # print(drink1["ingredients"])
# # # print(drink1["ingredients"][0])

# # people = [
# #   {
# #     "first_name": "Robert",
# #     "last_name": "Garcia",
# #     "hobbies": ["basketball", "chess", "phone tag"]
# #    },
# #    {
# #     "first_name": "Molly",
# #     "last_name": "Barker",
# #     "hobbies": ["programming", "reading", "jogging"]
# #    },
# #    {
# #     "first_name": "Kelly",
# #     "last_name": "Miller",
# #     "hobbies": ["cricket", "baking", "stamp collecting"]
# #    }
# # ]
# # # # # Write a loop to print out each person's hobby using a p statement, each on separate lines.

# # i = 0

# # while i < len(people):
# #   i_2 = 0
# #   while i_2 < len(people[i]["hobbies"]):
# #     print(people[i]["hobbies"][i_2])
# #     i_2 += 1
# #   i += 1

# # # # Write a loop to give each person an email address that consists of their first name + last name @ gmail.com. For example, Robert Garcia will have an email of robertgarcia@gmail.com.

# # # i = 0

# # while i < len(people):
# #   people[i]["email"] = people[i]["first_name"].lower() + people[i]["last_name"].lower() + "@gmail.com"
# #   i += 1

# # print(people)


# # items = [
# #   {
# #     "name": "Table",
# #     "price": 100,
# #     "description": "A nice wood dining room table."
# #   }
# # ]

# # print(items[0]["name"])
# # print(items[0]["price"])
# # print(items[0]["description"])


# # 1. Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.

# person = {"first_name": "John", "last_name": "Danger",
#           "email": "dangerjohn@gmail.com"}
# print(person["first_name"])
# print(person["last_name"])
# print(person["email"])


# # 2. Make an array of hashes to store the first name and last name for 3 different people. Then print out the first person's info.
# people = [{"first_name": "John", "last_name": "Danger", "email": "dangerjohn@gmail.com"}, {"first_name": "Kevin",
#                                                                                            "last_name": "Liger", "email": "lagerliger@gmail.com"}, {"first_name": "Hannah", "last_name": "Banana", "email": "banana@gmail.com"}]
# print(people[0])

# # 3. Make a hash to store prices for 3 different menu items. Then add a new menu item and price and print the hash to see the result.
# menu = {"fries": 7, "burger": 12, "cheese": 34}
# menu["ice cream"] = 11
# print(menu)
# 4. Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.
# book = {"author": "John Grisham", "title": "Murder Story Scary",
#         "page_count": 900, "language": "Spanish"}
# print(book["author"])
# print(book["title"])
# print(book["page_count"])
# print(book["language"])

# 5. Make an array of hashes to store the title and author for 3 different books. Then print out the third book's author.
books = [{"author": "John Grisham", "title": "Murder Story Scary",
          }, {"author": "Joseph Campbell", "title": "The Hero's Journey"}, {"author": "Fun McFungi", "title": "Fun Stuff"}]
print(books[2]["author"])

# 6. Make a hash to store 3 different states and their captitals. Then add a new state and capital and print the hash to see the result.
states = {"illinois": "Springfield",
          "Ohio": "Columbus", "Vermont": "Montpelier"}
states["Wisconsin"] = "Madison"
print(states)
# 7. Make a hash to store a laptop's brand, model, and year. Then print each attribute on separate lines.
laptop = {"brand": "Dell", "model": "Mac", "year": 2021}
print(laptop["brand"])
print(laptop["model"])
print(laptop["year"])
# 8. Make an array of hashes to store the brand and model for 3 different laptops. Then print out the second laptop's model.
laptop = [{"brand": "Dell", "model": "Mac", "year": 2021}, {"brand": "Mac",
                                                            "model": "Sick Mac", "year": 2010}, {"brand": "Dope Computer", "model": "Cool Comp", "year": 2212}]
print(laptop[1]["model"])

# 9. Make a hash to store definitions for 2 different words. Then add a new word and definition and print the hash to see the result.
words = {"music": "fun stuff that makes you dance",
         "cool": "the other side of the pillow"}
words["computer"] = "you can code and its great!!!"
print(words)
# 10. Make a hash to store a shirt's brand, color, and size. Then print each attribute on separate lines.
shirt = {"brand": "Adidas", "color": "Black", "size": "medium"}
print(shirt["brand"])
print(shirt["color"])
print(shirt["size"])

# SOLUTIONS: https://gist.github.com/peterxjang/d257aec07882d78009bd796ed53f81bb
