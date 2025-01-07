s = input()
n = len(s)
max_len = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        substr = s[i:j]
        if substr != substr[::-1]:
            max_len = max(max_len, len(substr))
print(max_len if max_len > 0 else 0)
