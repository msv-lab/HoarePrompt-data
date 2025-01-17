n_ = int(input())
for _ in range(n_):
    n = int(input())
    if n == 2:
        print('1 1')
        print('1 2')
    elif n == 3:
        print('2 1')
        print('2 3')
        print('3 1')
    elif n == 4:
        print('1 1')
        print('1 3')
        print('4 3')
        print('4 4')
    else:
        for i in range(1, n-1):
            print(f'1 {i}')
        print(f'{n} {n}')
        print(f'{n} 2')
    print()
