(n, m, k) = map(int, input().split())
area = n * m / k
if area != int(area):
    print('NO')
else:
    area = int(area)
    if area == 0:
        print('NO')
    else:
        print('YES')
        print('0 0')
        if 2 * area <= n:
            print(f'{2 * area} 1')
            print(f'0 1')
        elif 2 * area <= m:
            print(f'1 {2 * area}')
            print(f'1 0')
        else:
            print(f'{n} {m // 2}')
            print(f'0 {m // 2}')