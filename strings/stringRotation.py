def areRotations(s1,s2):
    if len(s1) != len(s2):
        return False
    temp = ' '
    temp = s1 + s1
    return temp.find(s2) != -1
if __name__ == "__main__":
    s1 = input("Enter String1")
    s2 = input("Enter String2")
    print(areRotations(s1,s2))