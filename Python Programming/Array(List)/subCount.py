def subCount(arr,k):
    res = 0
    n = len(arr)
    for i in range(n):
        curr = 0
        for j in range(i,n):
            curr = curr + arr[j]
            if curr % k == 0:
                res += 1
    return res
if __name__ == "__main__":
    arr = [4, 5, 0, -2, -3, 1]
    k = 5
    print(subCount(arr,k))