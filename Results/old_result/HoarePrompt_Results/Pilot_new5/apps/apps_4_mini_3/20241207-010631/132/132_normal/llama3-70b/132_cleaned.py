n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if sum(x) != sum(y):
    print('No')
else:
    x.sort()
    y.sort()
    if x == y:
        print('Yes')
    else:
        print('No')