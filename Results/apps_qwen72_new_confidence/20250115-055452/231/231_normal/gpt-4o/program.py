def check_for_length(S, length):
    seen = set()
    for i in range(len(S) - length + 1):
        substring = S[i:i + length]
        if substring in seen:
            return True
        seen.add(substring)
    return False

def find_max_length(S):
    left, right = 1, len(S)
    max_len = 0
    
    while left <= right:
        mid = (left + right) // 2
        if check_for_length(S, mid):
            max_len = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return max_len

# Read input
n = int(input())
s = input()

# Find and print the result
print(find_max_length(s))
