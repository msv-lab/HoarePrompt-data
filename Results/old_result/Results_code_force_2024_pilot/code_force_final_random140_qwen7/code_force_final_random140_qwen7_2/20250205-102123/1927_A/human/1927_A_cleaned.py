n = int(input())
for i in range(n):
    t = int(input())
    x = list(input())
    if 'B' in x:
        start = x.index('B')
        end = len(x) - x[::-1].index('B') - 1
        print(end - start)
    else:
        print(0)