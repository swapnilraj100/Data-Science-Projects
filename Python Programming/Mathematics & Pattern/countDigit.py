def countDigit(n):
    res = 0
    while n > 0 :
        n = n // 10
        res += 1
    return res
if __name__ == "__main__":
    n = int(input("Enter the number"))
    print(countDigit(n))