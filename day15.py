# day_15

'''
Repetition --> for, while

while
'''

# while simple usage 
'''
count = 0
while count <5:
    print("you can  acess ele")
    a = []
    a.append("codegnan")
    print(a)
    count+=1'''

# Checking vaild attempets
'''
count = 6
while count >=1:
    print(f"Count = {count}")
    count-=1
    print(count)
   

# To find valid password

password = input("Enter Password:")
while password == "admin":
    print(f'Correct Password--> Acess Granted')
    password = input("Enter the correct password")
print(f'Hurray its done-->Acess granted')
    
#give user a chance to type password again until he gives correct password
#Now give only 3 chances for password check -->if more than 3 print Account locked

password = input("Enter Password: ")
count = 1
while count <= 3:
    if password == "admin":
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        if count == 3:
            print("Account Locked")
            break
        password = input("Enter Password Again: ")
        count = count + 1


#for with else,which with else ---> else will be executed only when loop is completely done
#search for a product in the store

search = input("Enter the search item:").lower()
store = ["mobile","laptop","powerbank","charger"]
for item in store:
    if search == item:
        print(f'Item is found')
        break
else:
    print(f'Item is missing')

#tastask : PIN verification user should be given 3 chances if 3rd chance is over
#it should return Account locked for 24 hours --> balance withdrawl,show the number of chances

#push it to github and linkedin post


#break,continue,pass --> Jumoing statements
#break --> it terminates the loop once the given condition is satisfied

#continue --> it basically skips the current iteration and gets back to the next iteration

for i in "codegnan":
    if i == "g":
        continue
    print(i)
'''
#pass --> it is generally used as a placeholder (to have any syntax matches)

for i in range(10):
    pass
    print("hello")

class Class:
    pass








































