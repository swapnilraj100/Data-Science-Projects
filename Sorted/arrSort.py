#to check array is sorted
def checkarrSort(arr):
    n = len(arr)
    if (n == 0 or n == 1):
        return True
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            return False
    return True
if __name__ == "__main__":
    arr = [20, 23, 23, 45, 78, 88]
    print(checkarrSort(arr))