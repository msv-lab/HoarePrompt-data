# Read input values
n, k = map(int, input().split())
tab_types = list(map(int, input().split()))

# Function to calculate remaining tabs after closing every k-th tab starting from b
def calculate_remaining_tabs(b):
    remaining_tabs = tab_types[:]
    for i in range(b, n, k):
        remaining_tabs[i] = 0
    for i in range(b, -1, -k):
        remaining_tabs[i] = 0
    return remaining_tabs

max_diff = 0

# Iterate over each possible starting tab b
for b in range(n):
    remaining_tabs = calculate_remaining_tabs(b)
    e = remaining_tabs.count(1)
    s = remaining_tabs.count(-1)
    max_diff = max(max_diff, abs(e - s))

# Output the maximum absolute difference
print(max_diff)
