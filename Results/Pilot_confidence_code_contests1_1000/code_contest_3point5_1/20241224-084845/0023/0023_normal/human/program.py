n = input()
x, h = [0] * n, [0] * n
for i in range(n):
    x[i], h[i] = map(int, raw_input().split())

c = -2 * 10 ** 9
r = 0
for i in range(n):
    #print(i, r, c)
    if x[i] - h[i] > c:
        r += 1
        c = x[i]
        continue
    c = x[i]
    if i == n - 1 or x[i] + h[i] < x[i + 1]:
        c += h[i]
        r += 1
print(r)