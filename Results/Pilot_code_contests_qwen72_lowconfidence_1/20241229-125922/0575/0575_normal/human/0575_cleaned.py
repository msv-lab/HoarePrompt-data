num = int(raw_input())
for i in range(num):
    a = raw_input()
    b = raw_input()
    c = raw_input()
    f = 0
    for j in range(len(a)):
        if b[j] != c[j] and a[j] != c[j]:
            f = 1
            break
    if f == 0:
        print('YES')
    else:
        print('NO')