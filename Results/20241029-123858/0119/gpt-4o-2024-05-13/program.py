n = int(input())
segments = []

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))

# Sort segments by starting point, and in case of tie by ending point in descending order
segments.sort(key=lambda x: (x[0], -x[1]))

# We will keep track of the maximum ending point seen so far
max_right = -1
max_index = -1

for l, r, index in segments:
    # If the current segment's end is less than or equal to max_right, it means
    # there is a segment that completely contains the current segment
    if r <= max_right:
        print(index, max_index)
        break
    # Update the maximum ending point and its index
    max_right = r
    max_index = index
else:
    # If no such pair is found
    print(-1, -1)
