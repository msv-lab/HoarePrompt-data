n, k = map(int, input().split())
s = input()
t = input()

prefixes = 0
for i in range(n):
    if s[i] == t[i]:
        prefixes += 1
    else:
        break

possible_strings = 2 ** (n - prefixes)

max_c = prefixes * k + possible_strings * (k - 1)

print(max_c)