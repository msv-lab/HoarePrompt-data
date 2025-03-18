import sys
 
for _ in range(int(input())):
    n = int(input())
    #a, b = map(int, input().split())
    #a = list(map(int, input().split()))
    #s = str(input())
    mak = 0
    for i in range(1, n):
        print("?", mak, mak, i, i)
        sys.stdout.flush()
        if str(input()) == "<":
            mak = i
    mak2 = mak
    pans = []
    for i in range(n):
        print("?", mak, mak2, i, mak2)
        sys.stdout.flush()
        s = str(input())
        if s == "<":
            mak = i
            pans = [i]
        elif s == "=":
            pans.append(i)
    mak = 0
    for i in range(1, len(pans)):
        print("?", pans[mak], pans[mak], pans[i], pans[i])
        sys.stdout.flush()
        if str(input()) == ">":
            mak = i
    print("!", mak2, pans[mak])
    sys.stdout.flush()