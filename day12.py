#Problem 1 - Grade Checker

marks = int(input('Enter marks:'))

if marks > 100 or marks < 0:
     print('Invalid marks entered')
else:
     if marks >= 90:
          print('Grade: A')
          print('Remark: Outstanding!')
     elif marks >= 80:
          print('Grade: B')
          print('Remark: Excellent!')
     elif marks >= 70:
          print('Grade: C')
          print('Remark: Good!')
     elif marks >= 60:
          print('Grade: D')
          print('Remark: Fair, needs improvement')
     elif marks >= 50:
          print('Grade: E')
          print('Remark: Poor, needs serious improvement')
     else:
          print('Grade: F')
          print('Remark: Failed, needs to reappear')

#Problem 2 - Even-Odd Checker (with Twist)

number = int(input('Enter a number:'))

if number > 0:
     if number % 2 == 0:
          print('Even Number')
     else:
          print('Odd Number')
elif number < 0:
     if number % 2 == 0:
          print('Negative Even Number')
     else:
          print('Negative Odd Number')
else:
     print('Zero is neither even nor odd')

#Problem 3 - Season Identifier

season = int(input('Enter month number:'))

if season > 12 or season < 1:
     print('Invalid month number')
else:
     if season in (12,1,2):
          print('Season: Winter')
     elif season in (3,4,5):
          print('Season: Spring')
     elif season in (6,7,8):
          print('Season: Summer')
     else:
          print('Season: Autumn')
          
