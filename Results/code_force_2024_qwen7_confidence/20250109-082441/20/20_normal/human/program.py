from itertools import permutations

def find_minimum_core(s):
    min_core = s
    for permutation in permutations(s):
        core = find_core(''.join(permutation))
        if core < min_core:
            min_core = core

    return min_core

def find_core(s):
    max_substring = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring > max_substring:
                max_substring = substring

    return max_substring