def sumSubarray(arr,target):
    res = []
    n = len(arr)
    for s in range(n):
        curr = 0
        for e in range(s,n):
            curr = curr + arr[e]
            if curr == target:
                res.append(s+1)
                res.append(e+1)
                return res
    return [-1]
if __name__ == "__main__":
    #inarr = input("Enter Number")
    #arr = list(map(int,inarr.split()))
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    res = sumSubarray(arr,target)
    for i in res:
        print(i,end=" ")