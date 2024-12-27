input = lambda : stdin.readline().strip()
for _ in range(int(input())):
    (n, m) = [int(i) for i in input().split()]
    lst1 = [int(i) for i in input().split()]
    lst2 = [int(i) for i in input().split()]
    nk = 0
    lst1 = set(lst1)
    lst2 = set(lst2)
    for i in lst1:
        if i in lst2:
            print('YES')
            print(1, i)
            nk = 1
            break
    if nk == 0:
        print('NO')