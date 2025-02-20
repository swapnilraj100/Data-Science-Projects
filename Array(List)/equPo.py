def ePoint(arr):
    n = len(arr)
    for i in range(n):
        ls,rs = 0,0
        for j in range(i):
            ls += arr[j]
        for k in range(i+1,n):
            rs  += arr[k]
        if ls == rs:
            return True
    return False
if __name__ == "__main__":
    arr = [3,20,6,-8,4,-9]
    print(ePoint(arr))