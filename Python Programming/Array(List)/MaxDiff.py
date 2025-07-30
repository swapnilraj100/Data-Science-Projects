def MaxDiff(arr):
    n = len(arr)
    res = arr[1] - arr[0]
    minval = arr[0]
    for j in range(1,n):
        res = max(res,arr[j] - minval)
        minval = min(arr[j],minval)
    return res
if __name__ == "__main__":
    inarr = input("Enter Numbers")
    arr = list(map(int,inarr.split()))
    maxDiff = MaxDiff(arr)
    print(maxDiff)