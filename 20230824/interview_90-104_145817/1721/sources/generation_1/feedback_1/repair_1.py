def min_swaps_to_reverse_string(n, s):
    s = list(s)
    swaps = 0
    visited = set()
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if (s[i], s[n - i - 1]) not in visited:
                swaps += 1
                visited.add((s[i], s[n - i - 1]))
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
    return swaps

n = int(input())
s = input()
print(min_swaps_to_reverse_string(n, s))