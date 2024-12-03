n, k = map(int, input().split())
marks = list(map(int, input().split()))

total = sum(marks)
need = k * (n + x) - total

while need > 0:
    x += 1
    need -= k

print(x)
