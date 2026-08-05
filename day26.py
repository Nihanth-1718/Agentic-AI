"""
Day 26

Topics:
1. datetime Module
2. timedelta
3. time Module
4. Random Module
5. Rock Paper Scissors
6. QR Code Generation
"""

# ==========================================
# datetime Module
# ==========================================

from datetime import datetime, timedelta

print("========== Datetime Module ==========")

# Creating datetime object

date1 = datetime(2026, 8, 15)
print(date1)

date2 = datetime(day=16, month=9, year=2026, hour=10, minute=30)
print(date2)

# User Input

day = int(input("Enter the Day: "))
month = int(input("Enter the Month: "))
year = int(input("Enter the Year: "))

date_obj = datetime(year, month, day)

print("Date:", date_obj)
print("Day Name:", date_obj.strftime("%A"))
print("Month Name:", date_obj.strftime("%B"))

# Another Method

d, m, y = map(int, input("\nEnter Date (dd,mm,yyyy): ").split(","))

new_date = datetime(y, m, d)

print(new_date)
print("Day:", new_date.strftime("%A"))
print("Month:", new_date.strftime("%B"))

# ==========================================
# strptime()
# ==========================================

print("\n========== strptime ==========")

current = datetime.now()

old_date = datetime.strptime("26-12-1993", "%d-%m-%Y")

print(current)
print(old_date)

print(old_date.strftime("That day was %A"))

# ==========================================
# timedelta
# ==========================================

print("\n========== timedelta ==========")

difference = timedelta(days=5, hours=10)

print(difference)

print(current - difference)

print(current + difference)

print(current + timedelta(hours=5, minutes=30))

future = current + timedelta(hours=5, minutes=30)

print("Future Date:", future + timedelta(days=5, hours=10))

# ==========================================
# time Module
# ==========================================

import time

print("\n========== time Module ==========")

print(time.tzname)

print(time.ctime())

local = time.localtime()

print(f"Date is {local.tm_mday}-{local.tm_mon}-{local.tm_year}")

# ==========================================
# Rock Paper Scissors
# ==========================================

import random

print("\n========== Rock Paper Scissors ==========")

player1 = input("Enter Rock, Paper or Scissors: ").lower()

player2 = random.choice(["rock", "paper", "scissors"])

print("Computer Choice:", player2)

if player1 == "rock" and player2 == "paper":
    print("Computer Wins")
elif player1 == "paper" and player2 == "scissors":
    print("Computer Wins")
elif player1 == "scissors" and player2 == "rock":
    print("Computer Wins")
elif player1 == player2:
    print("It's a Tie")
else:
    print("Player Wins")

# ==========================================
# QR Code Generation
# ==========================================

import pyqrcode
import png

print("\n========== QR Code Generation ==========")

link = input("Enter the Link: ")

qr = pyqrcode.create(link)

filename = input("Enter File Name: ")

qr.png(filename + ".png", scale=15)

print("QR Code Generated Successfully")
