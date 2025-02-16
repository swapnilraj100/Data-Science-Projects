def lcm(a,b):
    res = max(a,b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res
if __name__ == "__main__":
    a = 4
    b = 6
    print(lcm(a,b))