n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
total_x = sum(x)
total_y = sum(y)
if total_y > total_x:
    print('No')
else:
    print('Yes')