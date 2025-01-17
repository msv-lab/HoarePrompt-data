for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()
    flag = "NO"
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            flag = "YES"
            break
    print(flag)