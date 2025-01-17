n = int(input())
a = list(map(int, input().split()))

# Function to find the maximum sum of a subarray
def max_subarray_sum(nums):
    max_so_far = float('-inf')
    current_max = 0
    
    for num in nums:
        current_max += num
        if max_so_far < current_max:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
    return max_so_far

# We need to find the segment where removing the smallest single card results in the maximum sum
max_score = float('-inf')

for i in range(n):
    left_sum = sum(a[:i])
    right_sum = sum(a[i+1:])
    current_score = left_sum + right_sum
    
    if current_score > max_score:
        max_score = current_score

# If all possible segments result in removing all cards, the score is 0
if max_score < 0:
    max_score = 0

print(max_score)
