def func_1(n, s):

    def is_cyclic_substring(t, s):
        t_extended = t + t
        return s in t_extended[:n + len(s) - 1]
    from itertools import product
    all_binary_strings = [''.join(p) for p in product('01', repeat=n)]
    count = 0
    for t in all_binary_strings:
        if is_cyclic_substring(t, s):
            count += 1
    return count
n = int(input())
s = input()
print(func_1(n, s))