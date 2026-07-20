'''sales = int(input())

if sales > 1000:
    print("Best Seller")
else:
    print("No Output")
'''

'''
Nested Conditions --> One condition inside another --> if ,else

Syntax:

if condition :
     if condition2:
          statement(s)..
          ....
    elif condition3...
         statement(s)....
         .....


#Usecase : ATM Withdrawl scenario
#Check Whether card is valid/not --> entered pin is correct or not --> check balance
#-->withdrawl
card = input("Card valid (yes/no): ")

if card == "yes":
    pin = int(input("Enter PIN: "))

    if pin == 1718:
        balance = 200000
        print("Available Balance:", balance)

        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Wrong PIN")
else:
    print("Invalid Card")
'''

#trip plan budget
budget = int(input("Enter your budget: "))

if budget > 10000:
    print("Plan: Trip")
elif budget > 5000:
    print("Plan: Resort Stay")
elif budget > 3000:
    print("Plan: Movie and Dinner")
elif budget > 1000:
    print("Plan: Cafe and Shopping")
elif budget > 500:
    print("Plan: Street Food and Park Visit")
else:
    print("Plan: Stay Home")

































