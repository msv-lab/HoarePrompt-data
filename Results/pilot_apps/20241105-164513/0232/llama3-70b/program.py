n, m = map(int, input().split())
colors = list(map(int, input().split()))
counts = list(map(int, input().split()))

color_counts = {}
for color in colors:
    if color not in color_counts:
        color_counts[color] = 0
    color_counts[color] += 1

found = False
for i in range(n):
    window_counts = {}
    for j in range(i, n):
        color = colors[j]
        if color not in window_counts:
            window_counts[color] = 0
        window_counts[color] += 1
        if all(count == target for count, target in zip(sorted(window_counts.values()), counts)):
            found = True
            break
    if found:
        break

print("YES" if found else "NO")
