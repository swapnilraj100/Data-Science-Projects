def InvTriangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
if __name__ == "__main__":
    InvTriangle(4)