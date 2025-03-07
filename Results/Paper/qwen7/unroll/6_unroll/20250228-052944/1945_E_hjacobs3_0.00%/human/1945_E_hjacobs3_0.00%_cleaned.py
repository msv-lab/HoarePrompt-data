def func_1(array, find):
    n = len(array)
    (l, r) = (0, n - 1)
    while l <= r:
        mid = (l + r) // 2
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
    if l != array.index(find):
        print(1)
        return [str(l + 1), str(array.index(find) + 1)]
    else:
        print(0)
t = int(input())
while t > 0:
    (n, x) = map(int, input().split(' '))
    array = [int(v) for v in input().split(' ')]
    res = func_1(array, x)
    if res:
        print(' '.join(res))
    t -= 1