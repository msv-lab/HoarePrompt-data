n, k = map(int, input().split())
absurdity = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)

# Calculate the prefix sum of absurdity
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + absurdity[i - 1]

max_total_absurdity = -1
a = b = 1

# Iterate through all possible segments
for i in range(1, n - k + 2):
    # Calculate the total absurdity of the first segment
    segment1_absurdity = prefix_sum[i + k - 1] - prefix_sum[i - 1]
    
    # Calculate the total absurdity of the second segment
    segment2_absurdity = prefix_sum[n] - prefix_sum[i + k - 1]
    
    # Calculate the total absurdity of two segments
    total_absurdity = segment1_absurdity + segment2_absurdity

    # Update the maximum total absurdity and the positions of the segments
    if total_absurdity > max_total_absurdity:
        max_total_absurdity = total_absurdity
        a = i
        b = i + k

print(a, b)