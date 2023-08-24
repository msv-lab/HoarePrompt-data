n = int(input())
ranges = []
for i in range(n):
    a, b = map(int, input().split())
    ranges.append((a, b))

ranges.sort(key=lambda x: x[0])
left_count = [0] * (n+1)
right_count = [0] * (n+1)
left_count[0] = 1
right_count[n] = 1

for i in range(1, n+1):
    left_count[i] = left_count[i-1] * (ranges[i-1][1] - ranges[i-1][0] + 1) % 1000000009
for i in range(n-1, -1, -1):
    right_count[i] = right_count[i+1] * (ranges[i][1] - ranges[i][0] + 1) % 1000000009

count = 0
for i in range(n):
    count += (left_count[i] * right_count[i+1]) % 1000000009
    count %= 1000000009

if count == 0:
    print("shovel time!")
else:
    print(count)
