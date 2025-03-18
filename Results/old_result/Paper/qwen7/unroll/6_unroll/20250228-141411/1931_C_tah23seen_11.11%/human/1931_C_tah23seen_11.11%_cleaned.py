def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
    if i > j:
        return 0
    while arr[i] == arr[i + 1]:
        i += 1
    if j != len(arr) - 1:
        return j - i + 1
    return j - i
t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    print(func_1(arr))
    t -= 1