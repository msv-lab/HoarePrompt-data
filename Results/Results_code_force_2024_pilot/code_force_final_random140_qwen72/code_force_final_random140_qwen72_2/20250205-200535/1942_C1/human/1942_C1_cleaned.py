if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        [n, x, y] = map(int, input().split())
        arr = input().split()
        arr = [int(arr[i]) for i in range(x)]
        arr.sort()
        arr.append(n + arr[0])
        ans = x - 2
        for i in range(1, x + 1):
            if arr[i] - arr[i - 1] == 2:
                ans += 1
        print(ans)