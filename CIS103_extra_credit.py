# Romain Tranchant
# CIS103
# Instructor: MD Ali
# Extra Credit Lab Assignment: Advanced Python Collections
# Due Date: 09/21/2024
# The objective of this lab is to challenge your understanding of Python’s collection types by
# applying them to real-world scenarios. You will work with lists, tuples, sets, and dictionaries to
# store, manipulate, and analyze data. The goal is to strengthen your ability to choose the right
# collection for a given task and perform advanced operations with these collections.


# Add a text file (or include in comments) describing any challenges you faced and how you
# overcame them
#
# Romain Tranchant : The main challenge I faced during this assignment was to use the proper synthax,
# to remember which operations to use for the right collections. For example, to add an element into
# a set, we use the add function, whereas in a list we have to use the append function.
# To make sure I use the proper synthax, I went back to the class course, went online to find any documentation
# and examples about any operations I had to perform.


# Part 1: Lists and Tuples
# 1. Task: Inventory Management System
# Imagine you are developing a game, and you need to create an inventory management system
# for the player’s equipment. Write a Python program that:
# - Creates a list called `inventory` with the following items: `'sword'`, `'shield'`, `'potion'`, `'bow'`,
# `'arrow'`, `'helmet'`.
# - The player finds a `'magic ring'`. Add it to the inventory list.
# - During battle, the `'potion'` is consumed. Remove it from the inventory.
# - The player upgrades their `'bow'` to a `'crossbow'`. Replace `'bow'` with `'crossbow'` in the list.
# - Print the updated inventory list.
# **Challenge (5 points):**
# - The player wants to sort their inventory alphabetically. Write code to sort the list.
# - The player is now carrying too much and wants to discard the first item on the list. Remove the
# first item and print the updated list.
# **Expected Output:**
# ['sword', 'shield', 'bow', 'arrow', 'helmet', 'magic ring']
# ['sword', 'shield', 'arrow', 'helmet', 'magic ring', 'crossbow']
# ['arrow', 'crossbow', 'helmet', 'magic ring', 'shield']

# Create an inventory list containing the initial items
inventory = ["sword", "shield", "potion", "bow", "arrow", "helmet"]

# Use the append() function to add magic ring to the list
inventory.append("magic ring")

# Use the remove() function to remove potion to the list and print the updated list
inventory.remove("potion")
print(inventory)

# Find the index of bow in the list and update bow by crossbow and print the updated list
inventory[inventory.index("bow")] = "crossbow"
print(inventory)

# Use the sort() function to sort the list in alphabetical order
inventory.sort()

# Use the del function to remove the first item from inventory, at index 0
# Print the updated list
del inventory[0]
print(inventory)

# 2. Task: Tuple Manipulation
# You have a tuple representing the stats of a video game character:
# `character_stats = (100, 50, 30)`
# The values represent health, attack, and defense points. Write a Python program that:
# - Prints the tuple.
# - Tuples are immutable. Create a new tuple `upgraded_stats` that increases the attack by 10 and
# defense by 5 (without modifying the original tuple).
# - Print both the original and upgraded stats.
# **Expected Output:**
# Original stats: (100, 50, 30)
# Upgraded stats: (100, 60, 35)

# Create a character's stats tuple and print the tuple using an f-string
character_stats = (100, 50, 30)
print(f"Original stats: {character_stats}")

# Convert the tuple into a list to allow changes
upgraded_stats = list(character_stats)

# Remove the second item, the attack value ,at index 1
upgraded_stats.pop(1)

# Insert a new attack value(60), at index 1, second item of the list
upgraded_stats.insert(1, 60)

# Remove the third value, defense, from the list at index 2
upgraded_stats.pop(2)

# Insert a new defense value(35), at index , third item of the list
upgraded_stats.insert(2, 35)

# Convert the list back into a tuple and print the updated tuple using an f-string
upgraded_stats = tuple(upgraded_stats)
print(f"Upgraded stats: {upgraded_stats}")


# Part 2: Sets and Dictionaries
# 1. Task: Unique Visitors Tracking
# Imagine you are tracking unique visitors to a website. Write a Python program that:
# - Creates a set called `visitors` with the following names: `'Alice'`, `'Bob'`, `'Charlie'`, `'Diana'`,
# `'Edward'`.
# - Two new visitors, `'Fiona'` and `'George'`, visit the website. Add them to the set.
# - `'Charlie'` visits the website again. Try to add `'Charlie'` to the set.
# - Remove `'Diana'` from the set (she unsubscribed).
# - Print the final set of unique visitors.
# **Challenge (5 points):**
# - Calculate and print the total number of unique visitors.
# **Expected Output:**
# {'Alice', 'Bob', 'Charlie', 'Diana', 'Edward'}
# {'Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George'}
# {'Alice', 'Bob', 'Charlie', 'Edward', 'Fiona', 'George'}
# Total unique visitors: 6

# Create a set with unique values and print the result
visitors = {"Alice", "Bob", "Charlie", "Diana", "Edward"}
print(visitors)

# Use the add() function to add Fiona and George to the set and print the updated set
visitors.add("Fiona")
visitors.add("George")
print(visitors)

# Use the remove() function to remove Diana from the set and print the updated set
visitors.remove("Diana")
print(visitors)

# Use the len() function to get the count of visitors, as sets cannot have duplicates,
# it will return the count of unique visitors. Print the count of visitors
# using an f-string
print(f"Total unique visitors: {len(visitors)}")

# 2. Task: Student Grades Dictionary
# Write a Python program to store and manipulate student grades using a dictionary. The
# dictionary should map student names to their grades. Start with the following dictionary:
# `student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 87, 'Diana': 78}`
# - Add a new student, `'Edward'`, with a grade of 90.
# - `'Bob'` has retaken an exam and improved his score to 95. Update Bob's grade.
# - Remove `'Diana'` from the dictionary (she dropped the course).
# - Calculate and print the average grade of all students remaining in the dictionary.
# **Challenge (5 points):**
# - Find and print the name of the student with the highest grade.
# **Expected Output:**
# {'Alice': 85, 'Bob': 95, 'Charlie': 87, 'Edward': 90}
# Average grade: 89.25
# Student with highest grade: Bob

# Create a dictionary of student grades
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 87, "Diana": 78}

# Add a new student's grade to the dictionary
student_grades["Edward"] = 90

# Update Bob's grade
student_grades["Bob"] = 95

# Delete Diana from the dictionary
del student_grades["Diana"]

# Print the updated dictionary
print(student_grades)

# Using the sum() to calculate the sum of all the values in the dictionary
sum_grades = sum(student_grades.values())

# Using the len() to get the count of students, they are they keys in this dictionary
number_student = len(student_grades.keys())

# Getting the mean of the grades by dividing the sum of the grades by the number of students
average_grade = sum_grades / number_student

# Print the mean as a float number using an f-string
print(f"Average grade: {float(average_grade)}")

# Use the max() to find the best grade, and get the key from the highest grade
max_grade = max(student_grades, key=student_grades.get)

# Print the name and the grade of the student with the highest grade using an f-string
print(f"Student with the highest grade: {max_grade}")


# Part 3: Real-World Scenario: Movie Database
# You are tasked with creating a simple movie database. You need to store information about each
# movie and its director. Write a Python program that:
# - Creates a dictionary where the keys are movie titles and the values are the directors' names.
# Start with the following movies:
# `movies = {'Inception': 'Christopher Nolan', 'Pulp Fiction': 'Quentin Tarantino', 'The Godfather':
# 'Francis Ford Coppola', 'The Dark Knight': 'Christopher Nolan'}`
# - Add two new movies: `'Interstellar'` by `'Christopher Nolan'` and `'Kill Bill'` by `'Quentin
# Tarantino'`.
# - A new version of `'The Godfather'` has been directed by `'Sofia Coppola'`. Update the director of
# `'The Godfather'` in the dictionary.
# - Print the entire updated movie database.
# **Challenge (5 points):**
# - Print all movies directed by `'Christopher Nolan'`.
# **Expected Output:**
# {'Inception': 'Christopher Nolan', 'Pulp Fiction': 'Quentin Tarantino', 'The Godfather': 'Sofia
# Coppola', 'The Dark Knight': 'Christopher Nolan', 'Interstellar': 'Christopher Nolan', 'Kill Bill':
# 'Quentin Tarantino'}
# Movies directed by Christopher Nolan: ['Inception', 'The Dark Knight', 'Interstellar']

# Create a dictionary of movies with their associated director
dictionary = {"Inception": "Christopher Nolan", "Pulp Fiction": "Quentin tarantino",
              "The Godfather": "Francis Ford Coppola", "The Dark Knight": "Christopher Nolan"}

# Add a new movie and director to the dictionary
dictionary["Interstellar"] = "Christopher Nolan"

# Add a new movie and director to the dictionary and print the updated dictionary
dictionary["The Godfather"] = "Sophia Coppola"
print(dictionary)

# Create an empty list called movies
movies = []

# Start a for loop to go through each keys and values of the dictionary
for keys, values in dictionary.items():

# If the value is "christopher Nolan", the key, the key or title of the movie
# will be returned into the movies list with the append()
    if values == "Christopher Nolan":
        movies.append(keys)

# Convert the movies list into a set to avoid duplicates
movies_set = set(movies)

# Print the result using an f-string
print(f"Movies directed by Christopher Nolan: {movies_set}")







