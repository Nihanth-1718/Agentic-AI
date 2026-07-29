"""
==========================================
Day 21 - Recursive & Anonymous Functions

Topics Covered:
1. Recursive Functions
2. Factorial using Recursion
3. Sum of Natural Numbers
4. Lambda Functions
5. Filter()
6. Map()
7. Reduce()
==========================================
"""

from functools import reduce

# ==========================================
# Recursive Function - Factorial
# ==========================================

print("========== Recursive Function : Factorial ==========")

def factorial(value):
    if value < 0:
        return "Enter a positive number"
    elif value == 0 or value == 1:
        return 1
    else:
        return value * factorial(value - 1)

user_number = int(input("Enter a number: "))
print("Factorial:", factorial(user_number))


# ==========================================
# Sum of Natural Numbers
# ==========================================

print("\n========== Sum of Natural Numbers ==========")

def calculate_sum(limit):
    if limit == 0:
        return 0
    return limit + calculate_sum(limit - 1)

sum_limit = int(input("Enter a number: "))
print("Sum:", calculate_sum(sum_limit))


# ==========================================
# Lambda Function - Rectangle Area
# ==========================================

print("\n========== Lambda Function ==========")

rect_length = int(input("Enter Length: "))
rect_width = int(input("Enter Breadth: "))

find_rectangle_area = lambda length_value, width_value: length_value * width_value
print("Rectangle Area:", find_rectangle_area(rect_length, rect_width))


# ==========================================
# Lambda Function - Square Area
# ==========================================

square_side = int(input("\nEnter Side of Square: "))

find_square_area = lambda side_value: side_value * side_value
print("Square Area:", find_square_area(square_side))


# ==========================================
# Lambda Function - Full Name
# ==========================================

given_name = input("\nEnter First Name: ")
family_name = input("Enter Last Name: ")

merge_name = lambda first_part, last_part: first_part + " " + last_part
print("Full Name:", merge_name(given_name, family_name))


# ==========================================
# Lambda Function - Even or Odd
# ==========================================

input_number = int(input("\nEnter a Number: "))

check_number = lambda num_value: "Even" if num_value % 2 == 0 else "Odd"
print(check_number(input_number))


# ==========================================
# Lambda Function - Length of String
# ==========================================

user_text = input("\nEnter a Message: ")

find_length = lambda sentence: len(sentence)
print("Length:", find_length(user_text))


# ==========================================
# Filter Function
# ==========================================

print("\n========== Filter Function ==========")

number_list = list(map(int, input("Enter Numbers (comma separated): ").split(",")))

filtered_even = list(filter(lambda item: item % 2 == 0, number_list))

print("Even Numbers:", filtered_even)


student_names = [
    "Pavan",
    "Abhiram",
    "Nihanth",
    "Saikiran",
    "Roshan",
    "Vasanthi",
    "Manimala"
]

filtered_names = list(filter(lambda person: len(person) > 6, student_names))

print("Names with length > 6:", filtered_names)


# ==========================================
# Map Function
# ==========================================

print("\n========== Map Function ==========")

programming_languages = ["python", "java", "agentic ai"]

capital_languages = list(map(lambda lang: lang.upper(), programming_languages))

print("Uppercase:", capital_languages)


price_list = [1000, 2500, 3500, 4000]

discounted_list = list(map(lambda amount: amount - (amount * 0.10), price_list))

print("Prices after 10% Discount:", discounted_list)


# ==========================================
# Reduce Function
# ==========================================

print("\n========== Reduce Function ==========")

number_values = [1, 4, 5, 7, 8]

total_sum = reduce(lambda first_value, second_value: first_value + second_value, number_values)
print("Sum:", total_sum)

total_product = reduce(lambda first_value, second_value: first_value * second_value, number_values)
print("Product:", total_product)
