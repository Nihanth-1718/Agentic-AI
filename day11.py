'''
Control Statements-->These are the statements which control the flow execution of the program

-->Conditional statements(if,else,elif)
-->Repetition Statements (Loops)-->For,while
-->Jumping Statements-->Break,continue,pass,assert
'''


#if statement:
'''

if<condition>:
   statements(s)...
   .........
   ........


#validate the price..
#money = 100
money = int(input("Enter the billing value:"))
if money <=100:
    print(f'Now you are eligible to get your items')
    print("Check again")



students = ['ram','akash','abhi','mani']
name = input("Enter the Student name:").lower()
if name in students:
    marks = 50
    grade = 'A'
    print(f'{name} has secured {marks} marks and {grade} Grade')



if-else statements...

syntax:
if condition:
    statements(s)
    .......
    ....
else:
    statements(s)
    ....
    ....


#vote eligiblity...
#user will enter his/her age--> give voter eligiblity
age = int(input("Enter the age:"))
if age>=18:
    print(f'you are eligible to vote so use properly')
    print("Your age is {} years,eligible".format(age))
else:
    print("You are not eligible to vote")
    print(f'You need to wait for {18-age} years to get vote right')


if-elif-else statements(s)....
'''
#For same above vote eligiblity we will rewrite the logic

age = int(input("Enter the age:"))
if age>=18:
    print(f'you are eligible to vote so use properly')
    print("Your age is {} years,eligible".format(age))
elif age==0 or age<0:
    print(f'Enter only +ve values')
else:
    print("You are not eligible to vote")
    print(f'You need to wait for {18-age} years to get vote right')
