n, k = map(int, input().split())
theorems = list(map(int, input().split()))
behavior = list(map(int, input().split()))

max_theorems = 0
current_theorems = 0
asleep_theorems = 0

# Calculate the initial theorems Mishka can write down
for i in range(n):
    if behavior[i] == 1:
        current_theorems += theorems[i]
    else:
        asleep_theorems += theorems[i]

# Store the maximum theorems Mishka can write down
max_theorems = current_theorems

# Use the secret technique
for i in range(n - k + 1):
    if behavior[i] == 0:
        asleep_theorems -= theorems[i]
    else:
        current_theorems -= theorems[i]
    
    if behavior[i + k] == 0:
        asleep_theorems += theorems[i + k]
    else:
        current_theorems += theorems[i + k]
    
    # Update the maximum theorems if necessary
    max_theorems = max(max_theorems, current_theorems + asleep_theorems)

print(max_theorems)