# Count of subarrays having sum equal to its length
def countSubArrLen(arr):
    res = 0
    n = len(arr)
    for i in range(n):
        csum = 0
        for j in range(i,n):
            csum = csum + arr[j]
            k = j - i + 1
            if csum == k:
                    res += 1
    return res
if __name__ == "__main__":
    arr = [1, 0, 2]
    print(countSubArrLen(arr))