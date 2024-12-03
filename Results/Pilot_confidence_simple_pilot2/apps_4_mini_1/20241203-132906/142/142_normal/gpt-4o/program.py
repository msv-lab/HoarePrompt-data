W = int(input())
cnt = list(map(int, input().split()))

# weights from 1 to 8
weights = [i for i in range(1, 9)]

# Initialize the max weight achievable to 0
max_weight = 0

# Iterate through each weight from 8 to 1
for i in range(7, -1, -1):
    if W >= weights[i]:
        # Calculate the maximum number of items of this weight we can use
        num_items = min(W // weights[i], cnt[i])
        # Update the total weight
        max_weight += num_items * weights[i]
        # Decrease the weight limit
        W -= num_items * weights[i]

print(max_weight)
