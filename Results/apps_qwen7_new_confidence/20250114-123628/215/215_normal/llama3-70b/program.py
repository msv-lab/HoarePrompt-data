s1 = input()
s2 = input()

n = len(s1)
res = 0
i = 0
while i < n:
    if s1[i] == '0' and s2[i] == '0':
        if i + 1 < n and s1[i + 1] == '0' and s2[i + 1] == '0':
            res += 1
            i += 2
        elif i + 2 < n and s1[i + 2] == '0' and s2[i + 2] == '0':
            res += 1
            i += 3
        else:
            i += 1
    else:
        i += 1
print(res)
