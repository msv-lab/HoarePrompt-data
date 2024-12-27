v1, v2 = map(int, input().split())
t, d = map(int, input().split())

max_speed = max(v1, v2)
min_speed = min(v1, v2)

max_length = max_speed * t
min_length = min_speed * t

for i in range(t-1, 0, -1):
    max_speed = max(max_speed - d, min_speed)
    min_speed = min(min_speed + d, max_speed)
    max_length += max_speed
    min_length += min_speed

print(max_length)
