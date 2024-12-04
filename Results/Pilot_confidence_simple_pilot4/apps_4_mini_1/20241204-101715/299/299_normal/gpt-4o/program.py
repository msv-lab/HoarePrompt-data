# Read input values
n, k = map(int, input().split())

# Determine if Sasha wins
if (n // k) % 2 == 1:
    print("YES")
else:
    print("NO")
