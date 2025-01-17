n, t = map(int, input().split())
total_glasses = n * (n + 1) // 2
full_glasses = 0
current_level = 1
current_glasses = 1
while full_glasses < total_glasses and t >= current_glasses:
    full_glasses += current_glasses
    t -= current_glasses
    current_level += 1
    current_glasses += 1
print(full_glasses)
