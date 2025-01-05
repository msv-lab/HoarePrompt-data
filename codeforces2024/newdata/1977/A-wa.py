cases = input()

for i in range(int(cases)):

    info = list(map(int, input().split()))

    if info[0] < info[1] or (info[1] - info[0] % 2 == 1):
        print("NO")
    else:
        print("YES")