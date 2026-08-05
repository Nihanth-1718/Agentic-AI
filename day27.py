"""
====================================================
Day 27 - File Handling & Exception Handling

Topics Covered:

1. File Handling
   - open()
   - read()
   - readline()
   - readlines()
   - write()
   - writelines()
   - File Modes (r, w, a, r+)

2. OS Module
   - exists()
   - getsize()
   - abspath()
   - listdir()

3. Exception Handling
   - try
   - except
   - finally
   - Multiple Exceptions

====================================================
"""

import os

# ==========================================
# Reading a File
# ==========================================

print("========== Reading a File ==========")

if os.path.exists("example.txt"):
    file = open("example.txt", "r")

    print(file.read())

    file.seek(0)
    print(file.readline())

    file.seek(0)
    print(file.readlines())

    file.close()
else:
    print("File Not Found")

# ==========================================
# File Information
# ==========================================

print("\n========== File Information ==========")

file_path = "example.txt"

if os.path.exists(file_path):
    print("File Exists")
    print("File Size :", os.path.getsize(file_path), "bytes")
    print("Absolute Path :", os.path.abspath(file_path))
else:
    print("File Not Found")

# ==========================================
# Write Mode
# ==========================================

print("\n========== Write Mode ==========")

with open("example.txt", "w") as file:
    file.write("Welcome to Python File Handling.\n")
    file.write("Today we are learning write mode.\n")
    file.writelines(["Python\n", "Agentic AI\n", "RAG\n"])

print("Content Written Successfully")

# ==========================================
# Append Mode
# ==========================================

print("\n========== Append Mode ==========")

with open("example.txt", "a") as file:
    file.write("This line is added using append mode.\n")

print("Content Appended Successfully")

# ==========================================
# Read and Write Mode
# ==========================================

print("\n========== Read & Write Mode ==========")

with open("example.txt", "r+") as file:
    print(file.read())
    file.write("\nLearning File Handling using Python.")

# ==========================================
# List All Text Files
# ==========================================

print("\n========== Text Files ==========")

files = os.listdir()

for file in files:
    if file.endswith(".txt"):
        print(file)

# ==========================================
# Exception Handling
# ==========================================

print("\n========== Exception Handling ==========")

try:
    num1, num2 = map(int, input("Enter two numbers separated by comma: ").split(","))

    result = num1 / num2

    print("Result :", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid integer values.")

finally:
    print("Program Executed Successfully.")

# ==========================================
# Multiple Exceptions Together
# ==========================================

print("\n========== Multiple Exceptions ==========")

try:
    a, b = map(int, input("Enter two numbers separated by comma: ").split(","))

    print("Division :", a / b)

except (ZeroDivisionError, ValueError) as error:
    print("Error :", error)

finally:
    print("Execution Completed.")
