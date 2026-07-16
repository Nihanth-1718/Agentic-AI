Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # String Creation
... name = "Codegnan"
... 
... print(name)
... print(len(name))
... print(type(name))
... 
... roll_no = "11QK1A0433"
... mobile_no = "8106429771"
... 
... print(len(roll_no))
... print(len(mobile_no))
... 
... # Concatenation
... place = "Hyd"
... course = "AAA"
... 
... print(name + course + place)
... print(f"We are in {course} class at {name} in {place}")
... 
... # Repetition
... data = "Agent"
... print(data * 3)
... print("*" * 25)
... 
... # Membership
... print("code" in "codegnan")
... print("agent" not in "Generative AI")
... 
... # Indexing
... name = "Codegnan"
... 
... print(name[0])
... print(name[4])
... print(name[-1])
... print(name[-4])
... 
... # Slicing
... print(name[:])
... print(name[1:])
... print(name[1:5])
... print(name[:5])
... print(name[5:])
... print(name[-5:])
... print(name[-5:-1])

# Step Slicing
print(name[::])
print(name[::2])
print(name[1:7:2])
print(name[::-1])
print(name[::-2])

# Built-in Functions
place = "Hyderabad"

print(len(place))
print(type(place))
print(min(place))
print(max(place))

print(ord("A"))
print(chr(97))

# String Methods
course = "Agentic ai"

print(course.lower())
print(course.upper())
print(course.title())
print(course.capitalize())
print(course.swapcase())

# Other Useful Methods
text = "  Python Programming  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(text.replace("Python", "Java"))
print(text.find("Programming"))
print(text.count("m"))

print("Python,Java,C++".split(","))
print("-".join(["Python", "Java", "C++"]))

print("python123".isalnum())
print("python".isalpha())
print("12345".isdigit())
print("python".islower())
print("PYTHON".isupper())
print("Python".startswith("Py"))
