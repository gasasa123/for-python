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



