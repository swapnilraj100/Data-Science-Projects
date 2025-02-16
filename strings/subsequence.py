def isSubSeq(s1,s2):
    i,j = 0,0
    while (i<len(s1) and j<len(s2)):
        if s1[i] == s2[j]:
            j += 1
        i += 1
    if j == len(s2):
        return True
    else:
        return False
if __name__ == "__main__":
    s1 = input("Enter String")
    s2 = input("Enter Subsequence")
    print(isSubSeq(s1,s2))
