def count_Substrings(s: str) -> int:
    count = 0
    n = len(s)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += int(s[j])
            if current_sum == (j - i + 1):
                count += 1
                
    return count

# Testing the function with the provided test cases
assert count_Substrings('112112') == 6
assert count_Substrings('111') == 6
assert count_Substrings('1101112') == 12
