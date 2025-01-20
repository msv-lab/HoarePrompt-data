n = int(input())
arr = list(map(int, input().split()))
increasing = False
constant = False
decreasing = False
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        if decreasing:
            print('NO')
            exit()
        increasing = True
    elif arr[i] == arr[i - 1]:
        if increasing:
            increasing = False
            constant = True
    else:
        if increasing:
            increasing = False
        decreasing = True
print('YES')