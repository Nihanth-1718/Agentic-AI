"""
==========================================
Day 18 - BMI Calculator & Functions

Topics Covered:
1. BMI Calculator
2. Exception Handling
3. Procedure Oriented Programming (POP)
4. User Defined Functions
5. Positional Arguments
6. Default Arguments
7. Keyword Arguments
==========================================
"""

# ==========================================
# BMI Calculator using Exception Handling
# ==========================================

while True:

    print("\n========== BMI Calculator ==========")
    print("1. Check BMI")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter your name: ")

        while True:

            try:
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (m): "))

                if weight <= 0 or height <= 0:
                    print("Please enter only positive values.\n")
                    continue

                bmi = weight / (height ** 2)

                print("\nBMI :", round(bmi, 2))

                if bmi < 18.5:
                    print(name, "-> Underweight")
                elif bmi < 25:
                    print(name, "-> Healthy Weight")
                elif bmi < 30:
                    print(name, "-> Overweight")
                else:
                    print(name, "-> Obesity")

                break

            except ValueError:
                print("Please enter valid numeric values.")

            except ZeroDivisionError:
                print("Height cannot be zero.")

    elif choice == 2:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


# ==========================================
# Procedure Oriented Programming
# User Defined Functions
# ==========================================

print("\n========== User Defined Functions ==========")


def add(a, b):
    """Returns the addition of two values"""
    return a + b


print(add(10, 20))
print(add("Code", "gnan"))
print(add([10, 20], [30, 40]))

result = add(100, 200)
print(result)


# ==========================================
# Positional Arguments
# ==========================================

print("\n========== Positional Arguments ==========")


def student(name, course):
    print("Name :", name)
    print("Course :", course)


student("Abhiram", "Python")


# ==========================================
# Default Arguments
# ==========================================

print("\n========== Default Arguments ==========")


def grocery(item, quantity=1):
    print("Item :", item)
    print("Quantity :", quantity)


grocery("Rice", 2)
grocery("Milk")


# ==========================================
# Keyword Arguments
# ==========================================

print("\n========== Keyword Arguments ==========")


def employee(name, company, role):
    print("Name :", name)
    print("Company :", company)
    print("Role :", role)


employee(role="Python Developer", company="Codegnan", name="Abhiram")
