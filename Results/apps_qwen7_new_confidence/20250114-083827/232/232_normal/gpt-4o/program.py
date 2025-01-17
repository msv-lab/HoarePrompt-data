# Read input
n, a = map(int, input().split())

# Calculate the minimum time to reach house a
if a % 2 == 1:
    # If a is odd, just return (a+1) // 2
    print((a + 1) // 2)
else:
    # If a is even, return (n - a + 2) // 2
    print((n - a + 2) // 2)
