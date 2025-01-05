(a, b) = map(float, raw_input().split())
if a < b:
    print - 1
    exit(0)
print(a + b) / (2 * math.floor((a + b) / (2 * b)))