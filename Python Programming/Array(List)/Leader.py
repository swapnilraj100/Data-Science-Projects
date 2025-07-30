def LeaderArray(arr):
    result = []
    n = len(arr)
    for i in range(n):
        is_leader = True
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
                result.append(arr[i])
    return result
if __name__ == "__main__":
    inarr = input("Enter array")
    arr = list(map(int,inarr.split()))
    resarr = LeaderArray(arr)
    print(resarr)