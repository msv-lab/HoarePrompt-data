def get_split(n, k):
    res = [0] * n
    if n == 1:
        return [k]
    else:
        msb = 0
        for i in range(31):
            if k & (1 << i):
                msb = i

        res[0] = 2 ^ msb - 1
        res[1] = k - res[0]

    return res


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(" ".join([str(num) for num in get_split(n, k)]))