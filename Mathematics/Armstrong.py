def isArmstrong(n):
    sum = 0
    num_dig = len(str(n))
    for i in str(n):
        sum = sum + int(i)**num_dig
    return sum == n
    
if __name__ == "__main__":
    n = int(input("Enter Number"))
    print(isArmstrong(n))