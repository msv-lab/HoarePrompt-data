def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        (n, a, b) = map(int, input().split())
        low = 0
        high = n
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if func_1(mid, a, b, n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans)