def squarePat(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
if __name__ == "__main__":
    squarePat(4)