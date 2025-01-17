# Read the input string
s = input()

# Length of the input string
n = len(s)

# List to store balance and position of each character in the input string
a = []

# List to store position and character of each character in the input string
b = []

# List to store the resultant sequence
c = [''] * n

# List to store the balance of each prefix in the resultant sequence
d = [0] * n

# Populate the list a with balance and position of each character
for i in range(n):
    a.append((s[:i].count('(') - s[:i].count(')'), i))

# Populate the list b with position and character of each character
for i in range(n):
    b.append((i, s[i]))

# Sort list a by balance and position in increasing order
a.sort()

# Sort list b by position in increasing order
b.sort()

# Reverse list b to match the order of a after sorting
b.reverse()

# Construct the resultant sequence
for i in range(n):
    # Determine the position of the current character in the resultant sequence
    c[a[i][1]] = b[i][1]
    # Update the balance of the prefix in the resultant sequence
    d[a[i][1]] = b[i][0]

# Print the resultant sequence
print(''.join(c))