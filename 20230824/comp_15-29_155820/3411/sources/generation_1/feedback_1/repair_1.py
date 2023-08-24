n, c, r = map(int, input().split())
scores = list(map(int, input().split()))

# Count the number of adjacent pairs with the same sign
same_sign_count = 0
for i in range(n-1):
    if scores[i] * scores[i+1] > 0:
        same_sign_count += 1

# Calculate the number of fake accounts needed to create an alternating chain
fake_accounts_needed = abs(same_sign_count - 1)

# Calculate the time required to create the fake accounts
fake_accounts_time = fake_accounts_needed * c

# Calculate the time required to remove comments
removal_time = r * same_sign_count

# Calculate the total time required
total_time = fake_accounts_time + removal_time

print(total_time)