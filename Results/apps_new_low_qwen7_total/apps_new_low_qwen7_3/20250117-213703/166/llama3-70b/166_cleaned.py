(b, d, s) = map(int, input().split())
print(max(0, b - d, b - s, d - s))