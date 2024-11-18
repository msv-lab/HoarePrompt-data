(x, y, z) = map(int, input().split())
if x > y + z:
    print('+')
elif x < y:
    print('-')
elif x == y:
    if z == 0:
        print('0')
    else:
        print('?')
else:
    print('?')