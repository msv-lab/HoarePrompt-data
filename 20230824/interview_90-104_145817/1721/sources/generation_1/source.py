def min_swaps_to_reverse_string(n, s):
    s = list(s)
    swaps = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            swaps += 1
    return swaps

n = int(input())
s = input()
print(min_swaps_to_reverse_string(n, s))