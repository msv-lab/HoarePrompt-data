t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split(' ')))
    if abs(a - b) % 2 == 0:
        print('Bob')
    else:
        print('Alice')