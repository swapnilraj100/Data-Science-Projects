def PatSearch(txt,pat):
    a = txt
    b = pat
    pos = a.find(b)
    while pos >= 0:
        print(pos)
        pos = a.find(b,pos+1)
if __name__ == "__main__":
    txt = input("Enter Text")
    pat = input("Enter Pattern")
    PatSearch(txt,pat)