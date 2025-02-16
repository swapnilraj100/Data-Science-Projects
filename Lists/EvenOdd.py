def getEvenOdd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l = [10,41,30,15,80]
e,o = getEvenOdd(l)
print(e)
print(o)