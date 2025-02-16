def removeDuplicates(arr):
    if not arr:
        return 0
    index = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[index]:
           index += 1
           arr[index] = arr[i]
    return index + 1
if __name__ == "__main__":
    l = [1,1,2,2,3,4,4,5]
    new_length = removeDuplicates(l)
    print(l[:new_length])