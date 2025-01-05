(n, r) = map(int, raw_input().split())
pi = 3.141592653589793
ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.sin(3 * pi / (2 * n)))
print(ans)