"""
==========================================
Day 20 - Pass by Value, Object Reference
& Built-in Functions
==========================================
"""

# ==========================================
# Pass by Value Reference (Immutable Objects)
# ==========================================

print("========== Pass by Value ==========")

def update_number(number):
    number = 15
    number = number * 5
    return number

value = 23

print(update_number(5))
print(update_number(value))
print(value)


def update_text(text):
    text = "Hi"
    text = text + " Bye"
    return text

name = "Nihanth"

print(update_text("Python"))
print(update_text(name))
print(name)


# ==========================================
# Pass by Object Reference (Mutable Objects)
# ==========================================

print("\n========== Pass by Object Reference ==========")

def update_list(data):
    data.append(30)
    return data

numbers = ["Abhi", 20, "AAA"]

print(update_list(numbers))
print(numbers)


def update_dict(student):
    student["Age"] = 21
    student["Name"] = "Ajith"
    return student

details = {"Name": "Abhi", "Age": 20}

print(update_dict(details))
print(details)


# ==========================================
# Built-in Functions
# ==========================================

print("\n========== Built-in Functions ==========")

print("Absolute :", abs(-23))

items = ["Python", "AI", "Agentic AI"]
print("All :", all(items))

items.clear()
print("All after clear :", all(items))

values = [None, 10, 20]
print("Any :", any(values))

print("Binary :", bin(10))
print("Character :", chr(65))
print("Boolean :", bool(1))
print("Complex :", complex())
print("Dictionary :", dict(name="Nihanth", course="Python"))

print("Divmod :", divmod(10, 3))

languages = ["Python", "Java", "C"]

print("Enumerate :", list(enumerate(languages)))
print("Enumerate from 1 :", list(enumerate(languages, 1)))

for index, language in enumerate(languages):
    print(index, ":", language)


# ==========================================
# Sorting & Other Built-in Functions
# ==========================================

print("\n========== More Built-in Functions ==========")

numbers = (23, 1, 4, 6)

print("Sorted :", tuple(sorted(numbers)))
print("Minimum :", min(numbers))
print("Maximum :", max(numbers))
print("Power :", pow(2, 3))
print("Reversed :", tuple(reversed(numbers)))
print("Round :", round(4.56))

courses = ["Codegnan", "AAA"]
years = [7, 1]

result = dict(zip(courses, years))
print("Zip :", result)
