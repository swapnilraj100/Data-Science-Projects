def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
if __name__ == "__main__":
    n = int(input("Enter Number"))
    fact = factorial(n)
    print(fact)