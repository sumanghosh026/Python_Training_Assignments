# <!-- Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found
 
 
# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
 
 
# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890 -->

import glob
import re

# Assignment 1
print("Assignment 1: .txt files containing the word 'Python'")
for filename in glob.glob("*.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        if re.search(r'\bPython\b', content, re.IGNORECASE):  # \b ensures it's a full word
            print(f"Found 'Python' in: {filename}")
print()


# Assignment 2
print("Assignment 2: Files starting with 'data_' and ending with '.csv'")
for filename in glob.glob("*"):
    if re.match(r'^data_.*\.csv$', filename):
        print(filename)
print()


# Assignment 3
print("Assignment 3: Valid phone numbers (format: (123) 456-7890)")

phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(123)456-7890",
    "(321) 654-0987",
    "(123 456-7890",
    "(123) 4567890"
]

for number in phone_numbers:
    if re.match(r'^\(\d{3}\) \d{3}-\d{4}$', number):
        print(number)
