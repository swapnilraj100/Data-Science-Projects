n = int(input("Enter Number"))
if n == 0:
    print(1)
if n == 1:
    print(1,1)
else:
    print(1,1,end=" ")
    x = 1
    y = 1
    for i in range(2,n+1):
        sum = x + y
        print(sum,end=" ")
        x = y
        y = sum