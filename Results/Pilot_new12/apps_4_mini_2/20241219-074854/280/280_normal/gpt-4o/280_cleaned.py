(v1, v2) = map(int, input().split())
(t, d) = map(int, input().split())
speeds = [0] * t
speeds[0] = v1
speeds[-1] = v2
for i in range(1, t):
    speeds[i] = min(speeds[i - 1] + d, v2 + (t - i - 1) * d)
total_distance = sum(speeds)
print(total_distance)