test_cases = int(input())
for i in range(test_cases):
    feat = [int(i) for i in input().split(' ')]
    n = feat[0]
    f = feat[1]
    a = feat[2]
    b = feat[-1]
    arr = [int(i) for i in input().split(' ')]
    array2 = []
    for i in range(1, n):
        if arr[i] - arr[i - 1] < b / a:
            array2.append((arr[i] - arr[i - 1]) * a)
    if sum(array2) + (n - len(array2)) * b < f:
        print('Yes')
    else:
        print('No')