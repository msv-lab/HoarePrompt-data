(a, b, c) = map(float, raw_input().split())
x = (a / b * c) ** 0.5
y = (b / c * a) ** 0.5
z = (c / a * b) ** 0.5
print(4 * (x + y + z))