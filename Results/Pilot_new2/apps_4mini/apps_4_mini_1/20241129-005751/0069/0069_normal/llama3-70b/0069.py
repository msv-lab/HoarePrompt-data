T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    s = input()
    cnt0, cnt1 = s.count('0'), s.count('1')
    balance = cnt0 - cnt1
    if balance == x:
        print(n + 1)
    elif (x - balance) % (cnt0 - cnt1) == 0:
        print(-1)
    else:
        print((x - balance) // (cnt0 - cnt1) + 1)
