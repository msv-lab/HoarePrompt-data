n = int(input())
numbers = list(map(float, input().split()))

# Sort the numbers in ascending order
numbers.sort()

# Round the first n numbers down and the last n numbers up
for i in range(n):
    numbers[i] = int(numbers[i])
    numbers[-(i+1)] = int(numbers[-(i+1)]) + 1

# Calculate the difference between the original sum and the adjusted sum
original_sum = sum(numbers) - n
adjusted_sum = sum(numbers)

# Calculate the minimum absolute difference
min_absolute_diff = abs(original_sum - adjusted_sum)

# Print the result with exactly three digits after the decimal point
print("{:.3f}".format(min_absolute_diff))