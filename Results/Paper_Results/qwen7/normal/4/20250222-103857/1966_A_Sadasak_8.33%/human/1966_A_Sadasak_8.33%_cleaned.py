def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        if frequency_table[num] > k:
            frequency_table[num] = k
    return frequency_table
t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    nums = list(map(int, input().split()))
    if k > n:
        print(n)
    elif k == n:
        print(k - 1)
    else:
        freq = func_1(nums, k)
        if k in freq.values():
            print(k - 1)
        else:
            print(n)