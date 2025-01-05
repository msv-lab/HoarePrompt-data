def solve(T, test_cases):
    for _ in range(T):
        n, a = test_cases[_][0], test_cases[_][1]
        f = sorted(test_cases[_][2])  # Sort numbers in ascending order
        s = [0] * (n + 1)  # Prefix sums, with s[0] = 0 for convenience

        # Calculate prefix sums
        for i in range(1, n + 1):
            s[i] = s[i - 1] + f[i - 1]  # Adjust index for 0-based in Python
        
        m = (s[n] - 1) // 2  # Maximum sum for any group to satisfy triangle inequality
        t = [0] * 3  # Sum of elements in each group
        v = [[] for _ in range(3)]  # Elements in each group

        y = True  # Flag to check if a valid grouping is possible
        for i in range(n - 1, -1, -1):  # Reverse iterate through numbers
            x = True  # Flag to check if current number can be placed
            for j in range(3):  # Check each group
                if a[j] and t[j] + f[i] + s[a[j] - 1] <= m:
                    v[j].append(f[i])  # Add number to group j
                    a[j] -= 1  # Decrease the count for group j
                    t[j] += f[i]  # Update the sum for group j
                    x = False  # Number placed successfully
                    break
            if x:  # If not able to place current number in any group
                print("NO")
                y = False
                break
        
        if y:  # If successfully placed all numbers
            print("YES")
            for group in v:
                print(" ".join(map(str, group)))

# Example usage
T = int(input())
test_cases = []
for _ in range(T):
    n, *a = map(int, input().split())
    f = list(map(int, input().split()))
    test_cases.append((n, a, f))

solve(T, test_cases)