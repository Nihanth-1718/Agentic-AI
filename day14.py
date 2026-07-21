'''
TypeConversions -> list,tuple,set,dict

list --> str,tuple,set,dict


age = [23,21,43]
age = list((21,21,43))
print(type(age))
#Every built-in datatype is a built-in function
b = str(age)
print(b)
print(len(b))
c = tuple(age)
print(type(c))
d = set(age)
print(d)
#e = dict(age) raises Typerror
#print(e)
e = dict.fromkeys(age)
print(e)

#str --> list,tuple,dict
name = 'codegnan'
print(type(name))
g = list(name)
print(g)
h = name.split()
print(h)
j = name.split(',')
print(j)
e = dict.fromkeys(name)
print(e)


#Input formatting --> list input,tuple input,dict input --> eval()
#list as input
data = eval(input("Enter the list:"))
print(data)
print(type(data))

data = eval(input("Enter the tuple values:"))
print(data)
print(type(data))

details = eval(input("Enter the student details :"))
print(details)
print(type(details))
'''

#Repetition Statements (Loops) --> for ,while
#loops will automate the tasks
'''
for loop is usedto iterate the items in a collection (str,list,tuple...) also can generate a sequence of numbers (range)

syntax for :

for <loop_var> in collection/range_function:
     statements(s)....
     .....

marks = [24,25,21,20]
for mark in marks:
    print(mark)
    print(mark,end='\t')


#Find the sum and average of marks

marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
summ = 0; avg = 0
for i in marks:
    #print(1)
    summ = summ + i
    print(summ)
    #print(summ)
    #avg = summ / len(marks)
print(f'Sum of given values is {summ}')
print(f'Avg of given values is {summ/len(marks)}')

#[1,2,3,4.5, 'codegnan',3,'agents',2.4]
#find the sum of the above list
data = eval(input("Enter the list:"))
sum = 0
for i in data:
    if type(i) == int or type(i) == float:
        sum = sum + i
print(f'sum of given values is {sum}')



details = {'names':['Sai', 'Abhi', 'Ram'],
           'marks':[24,20,28]}

print(details.items())
for i in details:
     print(i)
for key in details:
    print(key)

for value in details.values():
    print(value)

for key,value in details.items():
    print(f'Key is {key}')
    print(f'Value is {value}')

#range (start,end,step) --> generates a sequence of values
#range(end) #by default start is 0
for i in range(5):
    #print(i)
    print(f'Value of i is {i}')
#range(start,end)
for i in range (1,11):
    print(i,end=' ')
# range(start,end,step)
for i in range(1,11,2):
    print(i)
#In same way retrun numbers in reverse order
#10 8 6 4 2 0

for i in range(10, -1, -2):
    print(i, end=' ')
    
#home task print below patterns
#A B C D E F G H
#H F D B
'''

#daily workout log --> fitness streak
work_log = [1,1,1,0,1,1,0]
#Longest streak
longest_streak = 0
current_streak = 0
#for including if,else
# Daily Workout Log --> Fitness Streak
work_log = [1, 1, 1, 0, 1, 1, 0]
count = 0
max_count = 0
for i in work_log:
    if i == 1:
        count = count + 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)
































