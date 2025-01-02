from sys import maxint
n,t=map(int,raw_input().split())
arr=list(map(int,raw_input().split()))


def atMostSum(arr, n, k):
    _sum = 0
    cnt = 0
    maxcnt = 0

    for i in range(n):
        if ((_sum + arr[i]) <= k):
            _sum += arr[i]
            cnt += 1
        elif (sum != 0):
            _sum = _sum - arr[i - cnt] + arr[i]

        maxcnt = max(cnt, maxcnt)

    return maxcnt

print(atMostSum(arr,n,t))