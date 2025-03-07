def func_1(n, arr):
    arr.sort()
    new_arr = []
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            new_arr.append(arr[left])
        else:
            new_arr.append(arr[right])
            new_arr.append(arr[left])
        left += 1
        right -= 1
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
    return max_beauty
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = func_1(n, arr)
    results.append(result)
for result in results:
    print(result)