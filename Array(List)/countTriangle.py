def countTriangle(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and arr[j] + arr[k] > arr[i]:
                    res += 1
    return res
if __name__ == "__main__":
    arr = [4, 6, 3, 7]
    print(countTriangle(arr))