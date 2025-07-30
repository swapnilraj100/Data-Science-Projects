def decTobin(n):
    if n == 0:
        return "0"
    res = " "
    while n > 0:
        res = res + str(n%2)
        n = n // 2
    return res[::-1]
if __name__ == "__main__":
    n = int(input("Enter Decimal number"))
    bin = decTobin(n)
    print(bin)