def reverse(l):
    i = 0
    j = len(l) - 1
    while i < j:
        l[i],l[j] = l[j],l[i]
        i += 1
        j -= 1
if __name__ == "__main__":
    in_arr = input("Enter array sepated by space")
    arr = list(map(int,in_arr.split()))
    print(arr)
    reverse(arr)
    print(arr)