S = raw_input()
s0 = s1 = 0
for c in S:
    if c == '0':
        s0 += 1
    else:
        s1 += 1
print(max(s0, s1))