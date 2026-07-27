"""
==========================================
Day 19 - Advanced Functions & Variable Scope

Topics:
1. Variable Length Arguments (*args)
2. Keyword Variable Length Arguments (**kwargs)
3. BMI Calculator using Function
4. Local Variables
5. Global Variables
6. Global Keyword
7. Nonlocal Keyword
8. LEGB Rule
==========================================
"""

# ==========================================
# Variable Length Arguments (*args)
# ==========================================

print("========== Variable Length Arguments ==========")

def add(*numbers):
    """Returns sum of numeric values"""
    total = 0

    for value in numbers:
        if type(value) in (int, float):
            total += value

    return total


print(add())
print(add(10, 20))
print(add(10, 20, 30.5, "Python", 40))


# ==========================================
# Keyword Variable Length Arguments (**kwargs)
# ==========================================

print("\n========== Keyword Variable Length Arguments ==========")

def grocery(**items):
    """Displays grocery details"""

    for key, value in items.items():
        print(f"{key} : {value}")


grocery(
    Item="Milk",
    Price=35,
    Quantity="1 Litre",
    Brand="Heritage"
)


# ==========================================
# BMI Calculator using Function
# ==========================================

print("\n========== BMI Calculator ==========")

def bmi_calculator():

    while True:

        try:
            name = input("Enter Name: ")
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))

            if weight > 0 and height > 0:
                break
            else:
                print("Please enter only positive values.")

        except ValueError:
            print("Enter valid numeric values.")

    bmi = weight / (height ** 2)

    print("BMI :", round(bmi, 2))

    if bmi < 18.5:
        print(name, "-> Underweight")
    elif bmi < 25:
        print(name, "-> Healthy Weight")
    elif bmi < 30:
        print(name, "-> Overweight")
    else:
        print(name, "-> Obesity")


bmi_calculator()


# ==========================================
# Local Variable
# ==========================================

print("\n========== Local Variable ==========")

def company():
    company_name = "Codegnan"
    return company_name

print(company())


# ==========================================
# Global Variable
# ==========================================

print("\n========== Global Variable ==========")

company_name = "Codegnan"

def trainer():
    company_name = "Abhiram"
    return company_name

print(trainer())
print(company_name)


# ==========================================
# Global Keyword
# ==========================================

print("\n========== Global Keyword ==========")

count = 10

def update():
    global count
    count += 5
    return count

print(update())
print(count)


# ==========================================
# Nonlocal Keyword
# ==========================================

print("\n========== Nonlocal Keyword ==========")

def outer():

    value = 100

    def inner():
        nonlocal value
        value += 50
        print("Inner Value:", value)

    inner()
    print("Outer Value:", value)

outer()


# ==========================================
# LEGB Rule
# ==========================================

print("\n========== LEGB Rule ==========")

length = len("Codegnan")
print("Length :", length)
