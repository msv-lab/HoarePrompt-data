def can_break_shield(a, b, c):
    for x in range(c // a + 1):
        if (c - a * x) % b == 0:
            return True
    return False

# Read input
a, b, c = map(int, input().split())

# Check if it's possible to break the shield
if can_break_shield(a, b, c):
    print("Yes")
else:
    print("No")
