def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def printPrimeFactors(z):
    for i in range(2,z+1):
        if isPrime(i):
            x = i
            while z % x == 0:
                print(i,end=" ")
                x = x * i
if __name__ == "__main__":
    z = int(input("Enter Number"))
    printPrimeFactors(z)