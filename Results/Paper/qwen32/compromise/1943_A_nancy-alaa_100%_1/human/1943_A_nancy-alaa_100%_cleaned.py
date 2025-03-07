for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mpp = Counter(arr)
    first = False
    for i in range(n + 1):
        if i not in mpp.keys():
            print(i)
            break
        if mpp[i] == 1 and first:
            print(i)
            break
        if mpp[i] == 1:
            first = True