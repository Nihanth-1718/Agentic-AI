# Input Formatting

name = input("Enter your name: ")
print(name)
print(type(name))

age = int(input("Enter your age: "))
print(age)
print(type(age))

discount = float(input("Enter discount: "))
print(discount)
print(type(discount))

cp = int(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
print("Loss/Profit:", sp - cp)

name, place = input("Enter name and place: ").split()
print(name)
print(place)

name, place = input("Enter name,place: ").split(',')
print(name)
print(place)

a, b = map(int, input("Enter two integers: ").split(','))
print(a)
print(b)

x, y = map(float, input("Enter two floats: ").split(','))
print(x)
print(y)

data = input("Enter strings: ").split(',')
print(data)

marks = list(map(int, input("Enter marks: ").split(',')))
print(marks)

bmi = list(map(float, input("Enter BMI values: ").split(',')))
print(bmi)

# Output Formatting

print(25)
print(15, 2.5, "Codegnan")

print(2026, 7, 9)
print(25, 2.3, sep=',')
print(2026, 7, 9, sep='-')
print(2026, 7, 9, sep='/')
print("Codegnan", "AAA", sep=" <--> ")

name = "Codegnan"
place = "Hyderabad"
course = "Python"

print(name, place)
print(course)
print(name, place, end=' ')
print(course)
print(name, place, end='\t')
print(course)

print("Name:", name, "Place:", place)
print("Name:", name, "Place:", place, sep=',')

age = 32
place = "Hyd"
price = 458.63

print("Age is %d and Place is %s" % (age, place))
print("Item price is %f" % price)
print("Item price is %.0f" % price)
print("Item price is %.1f" % price)
print("Item price is %.2f" % price)

name = "Pavan"
course = "Python"

print("{} is enrolled in {} course".format(name, course))
print(f"{name} is enrolled in {course}")
print(f"{'Codegnan'}")
print("Codegnan")
