def func_1(n, k):
    positions = []
    i = 1
    while i <= n:
        positions.append(i)
        i += 2 * k + 1
    print(len(positions))
    print(' '.join(map(str, positions)))
(n, k) = map(int, input().split())
func_1(n, k)