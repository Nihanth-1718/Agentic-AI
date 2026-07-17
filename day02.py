Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Day 2 - Variables & Type Conversion
... 
... name = "Nihanth Sakalabhaktula"
... age = 21
... cgpa = 6.23
... 
... print(type(name), type(age), type(cgpa))
... 
... a, b = 10, 20
... a, b = b, a
... print("Swap:", a, b)
... 
... x = y = z = 100
... print(x, y, z)
... 
... print(float(age))
... print(int(cgpa))
... print(complex(age))
... print(bool(age), bool(0))
... 
... del x
... 
