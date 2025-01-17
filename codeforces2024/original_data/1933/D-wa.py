for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    b.sort()
    if b[1] == 1:
        print("NO")
    elif b[0] == 1:
        print("YES")
    else:
        for i in range(0, a):
            if b[i] % b[0] != 0:
                print("YES")
                break
        else:
            if b.count(b[0]) != a and a == 2:
                print("YES")
            else:
                print("NO")
