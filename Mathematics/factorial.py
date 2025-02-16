def fact(n):
    res = 1
    for i in range(2,n+1):
        res = res * i
    print("Factorial is" ,res)

if __name__ == "__main__":
    n = int(input("Enter Number"))
    fact(n)