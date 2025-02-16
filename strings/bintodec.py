def binTodec(b):
    res = 0
    p = 1
    for i in reversed(b):
        res = res + int(i)*p
        p = p*2
    return res
if __name__ == "__main__":
  bin = input("Enter Binary Number")
  dec = binTodec(bin)
  print(dec)