a, b, f, k = map(int, input().split())
if f > a - f:
    f = a - f
total_distance = a * 2
if b < f:
    print(-1)
else:
    num_refuel = (total_distance * k + b - 1) // b
    print(num_refuel)
