def reverseG(arr,k,n):
    i = 0
    while (i < n):
        left = i
        right = min(i+k-1,n-1)
        while (left < right):
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        i += k
if __name__ == "__main__":
    inarr = input("Enter Numbers")
    arr = list(map(int,inarr.split()))
    n = len(arr)
    k = int(input("Enter a number"))
    reverseG(arr,k,n)
    print(arr)