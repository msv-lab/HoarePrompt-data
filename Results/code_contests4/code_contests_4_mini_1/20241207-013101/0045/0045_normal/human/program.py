def main():
    n = int(input())
    d = {"S":[None]*13, "H":[None]*13, "C":[None]*13, "D":[None]*13}

    for i in range(n):
        x, y = raw_input().split()
        d[x][int(y)-1] = True

    for k in ["S", "H", "C", "D"]:
        for i in range(13):
            if d[k][i]:
                continue
            print("%s %d" % (k, i+1))

if __name__ == "main":
    main()