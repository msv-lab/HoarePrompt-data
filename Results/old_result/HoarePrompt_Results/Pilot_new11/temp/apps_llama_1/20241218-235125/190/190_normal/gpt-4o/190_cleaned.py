n = int(input())
a = list(map(int, input().split()))
min_cost = float('inf')
best_t = -1
for t in range(1, 101):
    current_cost = 0
    for length in a:
        if length < t - 1:
            current_cost += t - 1 - length
        elif length > t + 1:
            current_cost += length - (t + 1)
    if current_cost < min_cost:
        min_cost = current_cost
        best_t = t
print(best_t, min_cost)