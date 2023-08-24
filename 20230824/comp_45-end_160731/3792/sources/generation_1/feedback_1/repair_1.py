n, k = map(int, input().split())
s = input()
t = input()

prefixes = 0
for i in range(n):
    if s[:i+1] == t[:i+1]:
        prefixes += 1
    else:
        break

remaining_positions = n - prefixes

if s == t:
    max_c = prefixes * k
else:
    max_c = prefixes * k + (2 ** remaining_positions - 2) * (k - 1)

print(max_c)