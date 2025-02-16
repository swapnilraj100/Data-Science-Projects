def pallindrome(str):
    low = 0 
    high = len(str) - 1
    while low < high:
        if str[low] != str[high]:
            print("No")
            break
        low = low + 1
        high = high - 1
    print("Yes")

if __name__ == "__main__":
    str = input("Enter String")
    pallindrome(str)