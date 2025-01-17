t = int(input())
for i in range(0, t):
    n = int(input())
    s = set(map(int, input().split()))
    vals = list(s)
    if min(vals) != 1:
        print("Alice")
    elif len(vals) == 1:
        print("Alice")
    else:
        offset = 0
        vals.sort()
        while vals[offset] == (vals[offset + 1] - 1):
            offset += 1
            if offset == (len(vals) - 1):
                break
        if offset == (len(vals) - 1):
            offset += 1
        if offset % 2 == 0:
            print("Bob")
        else:
            print("Alice")