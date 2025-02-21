def RightRotate(arr,k):
    n = len(arr)
    k = k % n 
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
def reverse(arr,i,j):
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    k = 2
    RightRotate(arr,2)
    print(arr)
