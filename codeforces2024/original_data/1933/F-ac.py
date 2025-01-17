from collections import deque

# Process each test case
for _ in range(int(input())):
    y, x = map(int, input().split())  # Read dimensions of the grid

    # Initialize the dp table
    dp = []
    for _ in range(y):
        li = list(map(int, input().split()))
        for i in range(x):
            if li[i] == 1:
                li[i] = -1  # Mark rocks as -1
            else:
                li[i] = 1000000  # Initialize empty cells with a large number
        dp.append(li)

    dp[0][0] = 0  # Starting point

    queue = deque([(0, 0)])  # BFS queue starting from (0, 0)

    # Perform BFS
    while len(queue) > 0:
        i, j = queue.popleft()
        t = dp[i][j] + 1  # Time to reach the next cell

        # Check moving downwards cyclically
        if dp[(i+1) % y][j] != -1 and dp[(i+2) % y][j] != -1:
            if t < dp[(i+2) % y][j]:
                dp[(i+2) % y][j] = t
                queue.append(((i+2) % y, j))

        # Check moving right
        if j < x-1 and dp[(i+1) % y][j+1] != -1:
            if t < dp[(i+1) % y][j+1]:
                dp[(i+1) % y][j+1] = t
                queue.append(((i+1) % y, j+1))

    # Find the minimum time to reach the last column
    ans = 1000000
    for i in range(y):
        o = dp[i][x-1]
        if dp[i][x-1] == 1000000:
            continue
        p = (dp[i][x-1] - 1) % y

        if i < p:
            i += y
        ans = min(ans, i - p + o)

    # Output the result for the test case
    print(ans if ans != 1000000 else -1)