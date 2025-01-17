def count_distinct_cyclical_strings(n, s):
    # Function to check if string s is a substring of t or any of its cyclic permutations
    def is_cyclic_substring(t, s):
        t_extended = t + t
        return s in t_extended[:n + len(s) - 1]

    # Generate all binary strings of length n
    from itertools import product
    all_binary_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Count the number of distinct binary strings that contain s as a substring
    count = 0
    for t in all_binary_strings:
        if is_cyclic_substring(t, s):
            count += 1
    
    return count

# Reading input
n = int(input())
s = input()

# Printing the result
print(count_distinct_cyclical_strings(n, s))
