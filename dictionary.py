# Add populations to the city_populations hash for New York City (8.4 million) and San Francisco (800,000). The result should be:


# city_populations = {"Chicago": 2700000}

# city_populations["New York City"] = 8400000
# city_populations["San Francisco"] = 800000  


# print(city_populations)

####################



# Assume you have the following code:
# drink1 = {"name": "Seltzer", "ingredients": ["water", "bubbles"]}
# drink2 = {"name": "Coca Cola", "ingredients": ["water", "bubbles", "sugar", "brown food coloring"]}
# drink3 = {"name": "water", "ingredients": ["hydrogen", "oxygen"]}
# # Write a line of code to print out the name for drink1. Then write a line of code to print out the ingredients for drink1. Then write a line of code to print out only the first ingredient for drink1. The final output should be:
# # "Seltzer"
# # ["water", "bubbles"]
# # "water"

# print(drink1["name"])
# print(drink1["ingredients"])
# print(drink1["ingredients"][0])

people = [
  {
    "first_name": "Robert",
    "last_name": "Garcia", 
    "hobbies": ["basketball", "chess", "phone tag"]
   },
   {
    "first_name": "Molly",
    "last_name": "Barker",
    "hobbies": ["programming", "reading", "jogging"]
   },
   {
    "first_name": "Kelly",
    "last_name": "Miller",
    "hobbies": ["cricket", "baking", "stamp collecting"]
   }
]
# # # Write a loop to print out each person's hobby using a p statement, each on separate lines. 

i = 0

while i < len(people):
  i_2 = 0
  while i_2 < len(people[i]["hobbies"]):
    print(people[i]["hobbies"][i_2])
    i_2 += 1
  i += 1

# # Write a loop to give each person an email address that consists of their first name + last name @ gmail.com. For example, Robert Garcia will have an email of robertgarcia@gmail.com. 

# i = 0

while i < len(people):
  people[i]["email"] = people[i]["first_name"].lower() + people[i]["last_name"].lower() + "@gmail.com"
  i += 1

print(people)



items = [
  {
    "name": "Table",
    "price": 100,
    "description": "A nice wood dining room table."
  }
]

print(items[0]["name"])
print(items[0]["price"])
print(items[0]["description"])


