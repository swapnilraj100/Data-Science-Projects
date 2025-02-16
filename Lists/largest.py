def getMax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]
        return res
l = [10,5,20,8]
print(getMax(l))