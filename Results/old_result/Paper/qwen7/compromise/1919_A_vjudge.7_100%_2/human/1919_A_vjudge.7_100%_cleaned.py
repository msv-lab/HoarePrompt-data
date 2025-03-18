test = int(input())
for t in range(test):
    (a, b) = map(int, input().split())
    if a + b & 1 == 0:
        print('Bob')
    else:
        print('Alice')