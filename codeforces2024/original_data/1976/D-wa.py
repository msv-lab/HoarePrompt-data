def count_valid_pairs(s):
    n = len(s)
    prefix_balance = [0] * (n + 1)
    suffix_balance = [0] * (n + 1)
    balance_count = {}

    # Calculate prefix balance
    current_balance = 0
    for i in range(n):
        if s[i] == '(':
            current_balance += 1
        else:
            current_balance -= 1
        prefix_balance[i + 1] = current_balance

    # Calculate suffix balance
    current_balance = 0
    for i in range(n - 1, -1, -1):
        if s[i] == ')':
            current_balance += 1
        else:
            current_balance -= 1
        suffix_balance[i] = current_balance

    # Count valid pairs
    valid_pairs = 0
    for i in range(n):
        for j in range(i, n):
            if prefix_balance[i] == suffix_balance[j + 1]:
                valid_pairs += 1

    return valid_pairs

# Reading input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    s = data[index]
    index += 1
    results.append(count_valid_pairs(s))

# Output results
for result in results:
    print(result)