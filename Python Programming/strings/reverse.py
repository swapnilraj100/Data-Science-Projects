def reverse(str):
    rev = " "
    for i in str:
        rev = i + rev
    print(rev)
if __name__ == "__main__":
    str = input("Enter string")
    reverse(str)