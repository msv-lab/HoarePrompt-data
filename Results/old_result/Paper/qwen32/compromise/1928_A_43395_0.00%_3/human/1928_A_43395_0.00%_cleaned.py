for i in range(int(input())):
    (a, b) = [int(i) for i in input().split()]
    if a % 2 == 0 and b % 2 == 0:
        print('yes')
    elif (a - b == -a, a) or (b - a == -b, b):
        print('no')
    elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
        print('yes')
    else:
        print('no')