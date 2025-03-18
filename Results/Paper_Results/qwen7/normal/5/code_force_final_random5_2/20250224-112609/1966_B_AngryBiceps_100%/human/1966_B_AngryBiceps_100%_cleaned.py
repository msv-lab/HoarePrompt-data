for _ in range(int(input())):
    (n, m) = map(int, input().split())
    a = []
    first_row = ''
    last_row = ''
    for i in range(n):
        a.append(input())
        first_row += a[-1][0]
        last_row += a[-1][-1]
    if len(set(a[0])) == 1 and len(set(a[-1])) == 1 and (a[0] != a[-1]):
        print('NO')
    elif len(set(first_row)) == 1 and len(set(last_row)) == 1 and (first_row != last_row):
        print('NO')
    else:
        print('YES')