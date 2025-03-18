n = int(input())
s = input()
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for c in s:
    if c != '?':
        count[c] += 1
avg = n // 4
for c in 'ACGT':
    count[c] = avg - count[c]
res = ''
for c in s:
    if c == '?':
        for nc in 'ACGT':
            if count[nc] > 0:
                res += nc
                count[nc] -= 1
                break
    else:
        res += c
if any(count.values()):
    print('===')
else:
    print(res)