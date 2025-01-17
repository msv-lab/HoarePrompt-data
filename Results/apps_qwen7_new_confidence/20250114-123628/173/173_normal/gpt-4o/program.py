n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Initialize counters for academic performances in both groups
count_a = [0] * 6
count_b = [0] * 6

# Count the number of students with each academic performance in both groups
for performance in a:
    count_a[performance] += 1
for performance in b:
    count_b[performance] += 1

# Check if it's possible to achieve the desired distribution
for i in range(1, 6):
    if (count_a[i] + count_b[i]) % 2 != 0:
        print(-1)
        exit()

# Calculate the minimum number of exchanges
exchanges_needed = 0
for i in range(1, 6):
    # Calculate the difference for each academic performance
    diff = abs(count_a[i] - count_b[i]) // 2
    exchanges_needed += diff

# Since each exchange corrects the count for two students, we need to divide by 2
print(exchanges_needed // 2)
