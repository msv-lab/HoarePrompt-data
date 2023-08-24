a, b, c = map(int, input().split())

if a == 0 or b == 0:
    result = 2 * c + 1
else:
    result = 2 * c + 2

print(result)