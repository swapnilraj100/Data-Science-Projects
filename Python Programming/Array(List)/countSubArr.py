def countSubArray(arr,k):
    res = 0
    n = len(arr)
    for i in range(n):
        curr = 0
        for j in range(i,n):
            curr = curr + arr[j]
            if curr == k:
                res += 1
    return res
if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(countSubArray(arr,k))
