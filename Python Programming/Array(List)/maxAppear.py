def maxAppear(l,r):
    freq = [0] * 100
    for i in range(len(l)):
        for j in range(l[i],r[i]+1):
            freq[j] += 1
    return freq.index(max(freq))
if __name__ == "__main__":
    l = [1,2,15]
    r = [5,8,7,18]
    app = maxAppear(l,r)
    print(app)