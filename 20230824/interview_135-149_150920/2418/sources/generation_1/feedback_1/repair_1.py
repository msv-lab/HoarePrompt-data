# Read input values
n = int(input())
a = list(map(int, input().split()))
q = int(input())

# Initialize the sequence b and c
b = []
c = []
b.append(a[0])
c.append(a[0])

# Function to update the sequence b and c after a change
def update_sequence(l, r, x):
    for i in range(l-1, r):
        b[i] += x
        c[i] += x

# Function to find the minimum possible value of max(b_i, c_i)
def min_max_value():
    max_value = max(b[0], c[0])
    for i in range(1, n):
        max_value = min(max_value, min(b[i], c[i]))
    return max_value

# Print the initial minimum possible value of max(b_i, c_i)
print(min_max_value())

# Process each change and print the updated minimum possible value of max(b_i, c_i)
for _ in range(q):
    l, r, x = map(int, input().split())
    update_sequence(l, r, x)
    print(min_max_value())