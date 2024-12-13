n = int(input())
s = input()

# Initialize the number of stones to the minimum possible, which is zero.
stones = 0

# Process each operation
for operation in s:
    if operation == '+':
        stones += 1
    elif operation == '-':
        stones = max(0, stones - 1)

print(stones)
