def findSplitPoint(arr,n):
    left_sum = 0
    for i in range(0,n):
        left_sum += arr[i]
        right_sum = 0
        for j in range(i+1,n):
            right_sum += arr[j]
        if left_sum == right_sum:
            return i+1
    return -1
def pointTwoPart(arr,n):
    splitPo = findSplitPoint(arr,n)
    if (splitPo == -1 or splitPo == n):
        print("Not Possible")
        return 
    for i in range(0,n):
        if splitPo == i:
            print("")
        print(str(arr[i]) + '',end= ' ')
if __name__ == "__main__":
    arr = [1 , 2 , 3 , 4 , 5 , 5]
    n = len(arr)
    pointTwoPart(arr,n)