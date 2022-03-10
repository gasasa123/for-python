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




















