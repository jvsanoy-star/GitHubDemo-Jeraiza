# Activity 7.1
print("7.1. Activity 1: Understanding String Manipulation")
print("")

# Function for getting the uppercase version
def convert_upper(name):
    uppercase = name.upper()
    print("Uppercase: ", uppercase)

# Function for getting the lowercase version
def convert_lower(name):
    lowercase = name.lower()
    print("Lowercase: ", lowercase)

# Function for getting the length of the input
def get_length(name):
    length = len(name)
    print("Length: ", length)

# Ask the user for input
name = str(input("Please enter a name: "))

# Printing of output
print("\nOutput\n")
convert_upper(name)
convert_lower(name)
get_length(name)

# Activity 8.2
print("8.2. Activity 2: Understanding Date Manipulation")
print("")

import datetime

# Function to format the date as MM/DD/YY
def format_date(date_obj):
    return date_obj.strftime("%m/%d/%y")

# Function to get full month name
def get_month_name(date_obj):
    return date_obj.strftime("%B")

# Function to get weekday name
def get_weekday(date_obj):
    return date_obj.strftime("%A")

year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
day = int(input("Please enter the day: "))

# Create a date object
date_obj = datetime.date(year, month, day)

# Printing of output
print("\nOutput\n")
print(format_date(date_obj))
print(get_month_name(date_obj))
print(get_weekday(date_obj))
