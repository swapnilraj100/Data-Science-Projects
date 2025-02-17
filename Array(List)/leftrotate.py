def leftrotate(l,d):
    n = len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)
def reverse(l,i,j):
    while i < j:
        l[i],l[j] = l[j],l[i]
        i += 1
        j -= 1
if __name__ == "__main__":
    inarr = input("Enter numbers separated by space")
    arr = list(map(int,inarr.split()))
    print(arr)
    leftrotate(arr,4)
    print(arr)