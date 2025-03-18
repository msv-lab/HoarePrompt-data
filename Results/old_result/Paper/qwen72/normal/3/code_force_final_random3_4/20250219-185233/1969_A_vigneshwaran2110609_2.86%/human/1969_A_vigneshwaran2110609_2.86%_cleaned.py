n = int(input())
for i in range(n):
    x = int(input())
    l = list(map(int, input().strip().split()))
    for i in range(0, x):
        if l[l[i] - 1] == l[i] - 1:
            flag = True
            print(2)
            break
    else:
        print(3)