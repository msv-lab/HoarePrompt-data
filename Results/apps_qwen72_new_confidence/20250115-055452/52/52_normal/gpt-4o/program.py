def find_possible_message(t):
    n = len(t)
    for i in range(1, n):
        if t[:i] == t[-i:]:
            s = t[:-i]
            if s + t[-i:] == t:
                return "YES\n" + s
    return "NO"

# Read input
t = input().strip()

# Find and print the result
print(find_possible_message(t))
