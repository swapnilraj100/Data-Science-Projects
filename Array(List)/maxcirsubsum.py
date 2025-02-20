def maxCircularSum(arr):
    n = len(arr)
    res = arr[0]
    for i in range(0,n):
        curr_max = arr[i]
        curr_sum = arr[i]
        for j in range(1,n):
            index = (i+j) % n
            curr_sum += arr[index] 
            curr_max = max(curr_max,curr_sum)
        res = max(res,curr_max)
    return res
if __name__ == "__main__":
    arr = [10,14,11]
    res = maxCircularSum(arr)
    print(res)