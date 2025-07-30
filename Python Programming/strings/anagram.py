def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for i in count:
        if i != 0:
            return False
    return True
if __name__ == "__main__":
   s1 = input("Enter string 1")
   s2 = input("Enter string 2")
   print(areAnagram(s1,s2))