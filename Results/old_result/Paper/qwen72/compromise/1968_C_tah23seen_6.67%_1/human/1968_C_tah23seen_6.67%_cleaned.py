def func_1(arr, n):
    ans = [0] * n
    ans[0] = arr[0] + 1
    for i in range(n - 2):
        ans[i + 1] = arr[i] + ans[i]
        if ans[i + 1] < arr[i + 1]:
            while ans[i + 1] <= arr[i + 1]:
                ans[i + 1] += ans[i]
    ans[-1] = ans[-2] + arr[-1]
    return ans
t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    ans = func_1(arr, n)
    for i in ans:
        print(i, end=' ')
    print()
    t -= 1