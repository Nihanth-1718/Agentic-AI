"""
Day 20 - Python List Comprehensions & Generator Functions
Author : Nihanth Sakalabhaktula
"""

print("=" * 60)
print("DAY 20 - LIST COMPREHENSIONS & GENERATORS")
print("=" * 60)

# -------------------------------------------------------
# 1. Basic List Comprehension
# -------------------------------------------------------
print("\n1. Basic List Comprehension")

numbers = [i for i in range(10)]
print("Numbers :", numbers)

# -------------------------------------------------------
# 2. Square of Numbers
# -------------------------------------------------------
print("\n2. Square of Numbers")

squares = [i ** 2 for i in range(10)]
print("Squares :", squares)

# -------------------------------------------------------
# 3. Odd Number Check
# -------------------------------------------------------
print("\n3. Odd Number Check")

odd_check = [i % 2 == 1 for i in range(10)]
print(odd_check)

# -------------------------------------------------------
# 4. Convert Strings to Uppercase
# -------------------------------------------------------
print("\n4. String Conversion")

words = ["python", "codegnan", "agentic", "rag", "ai"]

upper_words = [word.upper() for word in words]

print("Original :", words)
print("Uppercase:", upper_words)

# -------------------------------------------------------
# 5. Update List Values
# -------------------------------------------------------
print("\n5. Add 5 to Every Element")

marks = [15, 20, 25, 35]

updated_marks = [i + 5 for i in marks]

print(updated_marks)

# -------------------------------------------------------
# 6. First Letter of Every Word
# -------------------------------------------------------
print("\n6. First Letter")

subjects = ["Python", "GenAI", "RAG", "Agents"]

letters = [i[0] for i in subjects]

print(letters)

# -------------------------------------------------------
# 7. List Comprehension with If
# -------------------------------------------------------
print("\n7. Using If Condition")

collection = [12, 7, 25, 4, 31, 18, 9]

even_numbers = [i for i in collection if i % 2 == 0]

print("Collection :", collection)
print("Even Numbers :", even_numbers)

# -------------------------------------------------------
# 8. Square of Collection
# -------------------------------------------------------
print("\n8. Square of Collection")

square_values = [i ** 2 for i in collection]

print(square_values)

# -------------------------------------------------------
# 9. Values Greater Than 10
# -------------------------------------------------------
print("\n9. Values Greater Than 10")

greater = [i for i in collection if i > 10]

print(greater)

# -------------------------------------------------------
# 10. If Else in List Comprehension
# -------------------------------------------------------
print("\n10. If Else")

status = ["Even" if i % 2 == 0 else "Odd" for i in collection]

print(status)

# -------------------------------------------------------
# 11. Nested List Comprehension
# -------------------------------------------------------
print("\n11. Nested List Comprehension")

pairs = [(i, j) for i in range(3) for j in range(3)]

print(pairs)

# -------------------------------------------------------
# 12. Multiplication Table
# -------------------------------------------------------
print("\n12. Multiplication Values")

table = [i * j for i in range(1, 5) for j in range(1, 5)]

print(table)

# -------------------------------------------------------
# 13. Dress Combinations
# -------------------------------------------------------
print("\n13. Dress Combinations")

colors = ["Red", "Blue", "Green"]
sizes = ["S", "M", "L"]

dress = [(c, s) for c in colors for s in sizes]

print(dress)

# -------------------------------------------------------
# 14. Nested List Comprehension with If
# -------------------------------------------------------
print("\n14. Nested If")

pairs = [(i, j) for i in range(5) for j in range(5) if i != j]

print(pairs)

# -------------------------------------------------------
# 15. Nested If Else
# -------------------------------------------------------
print("\n15. Nested If Else")

a = [1, 3, 5, 6, 7]
b = [2, 4, 6, 8, 9]

result = [x + 5 if x < y else x for x in a for y in b]

print(result)

# =======================================================
# GENERATOR FUNCTIONS
# =======================================================

print("\n" + "=" * 60)
print("GENERATOR FUNCTIONS")
print("=" * 60)

# -------------------------------------------------------
# 16. Normal Function
# -------------------------------------------------------

def normal_function():
    return [1, 2, 3, 4, 5]

print("\nNormal Function")

values = normal_function()

print(values)

for i in values:
    print(i)

# -------------------------------------------------------
# 17. Generator Function
# -------------------------------------------------------

def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print("\nGenerator Function")

gen = generator_function()

print(next(gen))
print(next(gen))
print(next(gen))

print("Remaining Values")

for value in gen:
    print(value)

# -------------------------------------------------------
# 18. Generator Example
# -------------------------------------------------------

def course_topics():
    yield "Python"
    yield "Generative AI"
    yield "RAG"
    yield "AI Agents"
    yield "FastAPI"

print("\nCourse Topics")

topics = course_topics()

for topic in topics:
    print(topic)

print("\nProgram Completed Successfully!")
