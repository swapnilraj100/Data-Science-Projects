def AllDivisors(n):
    i = 1
    while i * i < n:
        if n % i == 0:
            print(i,end=" ")
            print(n//i,end=" ")
        i += 1
if __name__ == "__main__":
    AllDivisors(100)