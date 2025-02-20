def maxEvenOdd(arr,n):
    res = 1
    for i in range(0,n):
        curr = 1
        for j in range(i+1,n):
            if (arr[j]%2==0 and arr[j-1]%2==0) or (arr[j]%2 != 0 and arr[j-1]%2 == 0):
                curr += 1
            else:
                break
        res = max(res,curr)
    return res
if __name__ == "__main__":
    arr = [5,10,20,6,3,8]
    n = len(arr)
    maxEO = maxEvenOdd(arr,n)
    print(maxEO)