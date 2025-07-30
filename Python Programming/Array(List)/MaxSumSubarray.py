def maxSum(arr,n):
    res = arr[0]
    for i in range(0,n):
        curr = 0
        for j in range(i,n):
            curr = curr + arr[j]
            res = max(res,curr)
    return res 
if __name__ == "__main__":
    inarr = input("Enter Number")
    arr = list(map(int,inarr.split()))
    n = len(arr)
    SubSum = maxSum(arr,n)
    print(SubSum)
