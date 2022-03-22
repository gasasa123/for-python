# 1
for i in range(1,20):
    if i%2!=0:
        print(i)

# 2
num = int(input("please enter number:"))
ch = int(input("please enter number 1 to odd number \nor number 2 to even number :"))
if ch == 1:
    for i in range(1,num,2):
        print(i)
elif ch == 2:
    for i in range(0,num,2):
        print(i)
else:
    print("Insert numbers 1 or 2")

# 3
i = 100
for i in range(100,500):
    if i == 287:
        print(i)
        break

# 4
i=0
for i in range(10,20):
    flag=0
    if i != 13:
        print(i)
        i+=1

# 5
sum = 0
for i in range(1,14):
   sum=sum+i
   print(sum)

# 6
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=' ')
    print()

# 7
for i in range(100,5000,4):
    print(i)

# 8
for i in range(5,2500):
    if i %6==0:
        print(i)

# 9
name = input("please enter your nane :")
for letter in name :
    print(letter, end = "")

# 10
rows = int(input("Please Enter the Total Number of Rows  : "))
columns = rows - 4
if rows < 4 :
    print("please enter a number larger then 4")
else:
    for i in range(rows):
        for j in range(columns):
            print('*', end = '  ')
        print()

# 11
x = input("enter 5 digit nun:",)
y = input("enter 5 digit nun:")
for (i,j) in zip(x,y):
    if i == j:
        print (i)
# 12
sum=0
for x in range(0,50):
    sum+=x
print("sum is:",sum)

# 13
sum=0
for x in range(100,250,3):
    sum+=x
print("sum is:",sum)

# 14
sum=0
for x in range(1000,5000,7):
    sum+=x
print("sum is:",sum)

# 15
sum = 1
for x in range(5,20):
    sum*=x
print("sum is:",sum)

# 16
sum = 1
for x in range(15,35,2):
    sum*=x
print("sum is:",sum)

# 17
num=int(input("please enter number:"))
for i in range (num):
    if i % 2 == 0:
        print(i)

# 18
num=int(input("please enter number:"))
for i in range (num):
    if i % 7 != 0:
        print(i)
    if i % 7 == 0 :
        print("boom")

# 19
num = 0
for i in range (1,20):
    if i%2==0:
        print(i)