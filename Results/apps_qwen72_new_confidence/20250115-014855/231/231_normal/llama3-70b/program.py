N = int(input())
S = input()

max_len = 0
for len in range(1, N // 2 + 1):
    for i in range(N - len):
        substr = S[i:i + len]
        if S.count(substr) > 1 and i + len <= S.index(substr, i + 1):
            max_len = max(max_len, len)

print(max_len)
