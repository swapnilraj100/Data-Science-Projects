def sumSubarray(arr):
    res = arr[0]
    n = len(arr)
    for i in range(0,n):
        currSum = 0
        for j in range(i+1,n):
            currSum = currSum + arr[j]
            res = max(res,currSum)
    return res
if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    maxsum = sumSubarray(arr)
    print(maxsum)