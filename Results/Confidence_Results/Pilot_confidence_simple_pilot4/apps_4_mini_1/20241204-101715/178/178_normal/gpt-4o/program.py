k = int(input())

# Determine the length of numbers we are currently considering
length = 1
count = 9
start = 1

# Find the range in which the k-th digit lies
while k > length * count:
    k -= length * count
    length += 1
    count *= 10
    start *= 10

# Find the exact number where the k-th digit is located
start += (k - 1) // length
s = str(start)
result = s[(k - 1) % length]

print(result)
