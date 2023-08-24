n = int(input())
snow_ranges = []
for i in range(n):
    lower_limit, upper_limit = map(int, input().split())
    snow_ranges.append((lower_limit, upper_limit))

snow_ranges.sort(key=lambda x: x[0])
left_count = [1] * (n+1)
right_count = [1] * (n+1)

for i in range(1, n+1):
    snow_level = snow_ranges[i-1][1] - snow_ranges[i-1][0] + 1
    left_count[i] = (left_count[i-1] * snow_level) % 1000000009

for i in range(n-1, -1, -1):
    snow_level = snow_ranges[i][1] - snow_ranges[i][0] + 1
    right_count[i] = (right_count[i+1] * snow_level) % 1000000009

count = 0
for i in range(n):
    count += (left_count[i] * right_count[i+1]) % 1000000009
    count %= 1000000009

if count < 3:
    print("shovel time!")
else:
    print(count)