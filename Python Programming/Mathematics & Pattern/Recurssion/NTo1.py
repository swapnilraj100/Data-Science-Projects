def PrintNto1(num):
    if num <=0:
        return 
    print(num,end=" ")
    PrintNto1(num-1)
def Print1toN(num):
    if num <=0:
        return
    Print1toN(num-1)
    print(num,end=" ")
if __name__ == "__main__":
    num = int(input("Enter Number"))
    PrintNto1(num)
    print()
    Print1toN(num)