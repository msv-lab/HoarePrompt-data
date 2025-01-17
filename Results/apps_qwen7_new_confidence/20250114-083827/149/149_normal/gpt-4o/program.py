# Read input
n, a, x, b, y = map(int, input().split())

# Simulate the movement of Daniel and Vlad
while True:
    if a == b:  # If Daniel and Vlad meet at the same station
        print("YES")
        break
    if a == x or b == y:  # If either of them reaches their destination
        print("NO")
        break
    # Move Daniel to the next station in clockwise direction
    a = a + 1 if a < n else 1
    # Move Vlad to the next station in counterclockwise direction
    b = b - 1 if b > 1 else n
