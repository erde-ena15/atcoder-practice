def main():
    y,m,d = input().split("/")
    y = int(y)
    if m[0] == "0":
        m = int(m[1])
    else:
        m = int(m)   
    if d[0] == "0":
        d = int(d[1])
    else:
        d = int(d)   
    if y <= 2019 and m <= 4 and d <= 30:
        print("Heisei")
    else:
        print("TBD")
main()