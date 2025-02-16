def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for i in l[1:]:
        if i > lar:
            slar = lar
            lar = i
        elif i != lar:
            if slar == None or slar < i:
                slar = i
    return slar
if __name__ == "__main__":
    l = [10,5,8,20]
    slar = getSecMax(l)
    print(slar)