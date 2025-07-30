def FindMajority(arr,n):
    for i in range(0,n):
        count = 1
        for j in range(i+1,n):
            if arr[i] == arr[j]:
               count += 1
        if count > n//2:
            return arr[i]
    return -1
if __name__ == "__main__":
    arr = [1,1,2,1,3,5,1]
    n = len(arr)
    maj = FindMajority(arr,n)
    print(maj)