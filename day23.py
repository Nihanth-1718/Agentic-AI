"""
====================================================
Day 23 - Modules

Topics Covered:

1. User Defined Modules
   - Creating a Module
   - Accessing a Module
   - import module_name
   - from module_name import function
   - from module_name import function1, variable
   - from module_name import *

2. Built-in Modules
   - math
   - os
   - sys
   - random

====================================================
"""

# ==========================================
# User Defined Module Concept
# ==========================================

def welcome(user_name):
    """Greeting Function"""
    return f"Hello {user_name}"


student_info = {
    "Student_Names": ["Nihanth", "Rahul", "Sai"],
    "Student_Ages": [21, 22, 23]
}


def course_generator():
    """Generator Function"""
    yield "Python"
    yield "GenAI"
    yield "RAG"
    yield "Agents"


print("========== User Defined Module ==========")

print(welcome("Nihanth"))

print(student_info)

student_info.update({"Location": "Hyderabad"})
print(student_info)

course_data = course_generator()

print(next(course_data))
print(next(course_data))
print(next(course_data))
print(next(course_data))

# ==========================================
# Different Ways to Import Modules
# ==========================================

"""
Method 1:
import module_name

import MY
print(MY.welcome("Nihanth"))
print(MY.student_info)
"""

"""
Method 2:
from module_name import function_name

from MY import welcome
print(welcome("Nihanth"))
"""

"""
Method 3:
from module_name import function_name, variable

from MY import welcome, student_info
print(welcome("Nihanth"))
print(student_info)
"""

"""
Method 4:
from module_name import *

from MY import *
print(welcome("Nihanth"))
print(student_info)
"""

# ==========================================
# Built-in Module - math
# ==========================================

import math

print("\n========== Math Module ==========")

print("Ceil:", math.ceil(2.5))
print("Floor:", math.floor(2.9))
print("e:", math.e)
print("exp(2):", math.exp(2))
print("Factorial:", math.factorial(6))
print("Float Modulus:", math.fmod(5, 2))
print("log(1):", math.log(1))
print("log10(100):", math.log10(100))
print("log2(8):", math.log2(8))
print("modf:", math.modf(5.3))
print("Pi:", math.pi)
print("Power:", math.pow(5, 3))
print("Truncate:", math.trunc(6.8))

# ==========================================
# Built-in Module - os
# ==========================================

import os

print("\n========== OS Module ==========")

print("Current Working Directory:")
current_directory = os.getcwd()
print(current_directory)

print("\nFiles in Current Directory:")
directory_files = os.listdir()
print(directory_files)

# Uncomment to create/remove a directory

# os.mkdir("sample")
# os.removedirs("sample")

# ==========================================
# Built-in Module - sys
# ==========================================

import sys

print("\n========== SYS Module ==========")

print("Python Version:")
python_version = sys.version
print(python_version)

print("\nPython Path:")
python_paths = sys.path
print(python_paths)

# ==========================================
# Built-in Module - random
# ==========================================

import random

print("\n========== Random Module ==========")

random_float = random.random()
print("Random Float:", random_float)

random_number = random.randint(1, 100)
print("Random Integer:", random_number)

print("\nOTP Generation")

for otp_count in range(5):
    otp_code = random.randint(1000, 9999)
    print(otp_code)
