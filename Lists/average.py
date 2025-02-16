def average(l):
    sum = 0
    for i in l:
        sum = sum + i
    n = len(l)
    return sum/n
l = [10,60,50,40]
print(average(l))