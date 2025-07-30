def dSum(num):
    if num <= 0:
        return 0
    else:
        return dSum(num // 10) + abs(num) % 10
if __name__ == "__main__":
    num = int(input("Enter Number"))
    digitSum = dSum(num)
    print(digitSum)