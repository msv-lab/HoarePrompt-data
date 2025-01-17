def min_lex_rotation(s):
    """ Returns the lexicographically smallest rotation of the string s. """
    s = s + s  # Concatenate string to itself
    n = len(s) // 2
    start = 0
    for i in range(1, n):
        for j in range(n):
            if s[start + j] != s[i + j]:
                if s[start + j] > s[i + j]:
                    start = i
                break
    return s[start:start + n]

def unique_strings(n, c, k):
    MOD = 10**9 + 7
    unique_rotations = set()
    
    # Iterate over the number of ones we can have
    for ones in range(c, c + k + 1):
        if ones > n:
            break
        # Generate all strings with `ones` number of 1s
        zeros = n - ones
        from itertools import combinations
        for positions in combinations(range(n), ones):
            s = ['0'] * n
            for pos in positions:
                s[pos] = '1'
            s = ''.join(s)
            # Get the minimum lexicographical rotation
            min_rotation = min_lex_rotation(s)
            unique_rotations.add(min_rotation)
    
    return len(unique_rotations) % MOD

# Example usage:
n, c, k = map(int, input().split())
print(unique_strings(n, c, k))