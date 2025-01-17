k = int(input())

# Step 1: Determine the length of the number where the k-th digit lies
length = 1
count = 9
start = 1

while k > length * count:
    k -= length * count
    length += 1
    count *= 10
    start *= 10

# Step 2: Determine the exact number and digit within that number
number = start + (k - 1) // length
digit_index = (k - 1) % length

# Step 3: Convert the number to string and get the digit
result = str(number)[digit_index]

print(result)
