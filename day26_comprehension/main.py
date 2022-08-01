# For list comprehension think of the keywords:
# new_list = [new_item for item in list if test]

# list comprehension to square each number in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

# list comprehension to get only even numbers from a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

# list comprehension on a list of strings
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
long_names = [n.upper() for n in names if len(n) > 5]
print(short_names)
print(long_names)

# Read from two files and use list comprehension to get common numbers from each
with open('file1.txt', mode='r') as file1:
    f1_list = file1.readlines()

with open('file2.txt', mode='r') as file2:
    f2_list = file2.readlines()

print(f1_list)
print(f2_list)
common = [int(n) for n in f1_list if n in f2_list]
print(common)

# Dictionary comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: for (key, value) in dict.items()}
import random
student_scores = {student: random.randint(50, 100) for student in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score > 70}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

temp_celsius = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

temp_farenheit = {day: (temp_c * 9/5)+32 for (day, temp_c) in temp_celsius.items()}
print(temp_farenheit)

# Looping through a dataframe
import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_df = pd.DataFrame(student_dict)
print(student_df)
# Loop through rows of a dataframe
new_dict = {row.student: row.score for (index, row) in student_df.iterrows()}
print(new_dict)
