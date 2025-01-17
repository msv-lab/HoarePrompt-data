def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        a, b = map(int, input().split())
        # Check if the area is even or odd
        if (a * b) % 2 == 0:
            print("Yes")
        else:
            print("No")

# Example usage
solve()
