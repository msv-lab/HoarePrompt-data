t = int(input())
for _ in range(t):
    v = list(map(int, input().split()))
    if (v[0] + v[1] + v[2]) % 2 == 1:
        print('-1')
    else:
        result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
        print(result)