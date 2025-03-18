s = input()
vowels = set('aeiou')
ans = []
tmp = []
for c in s:
    if c in vowels or (tmp and tmp[-1] == c):
        tmp.append(c)
    else:
        if len(tmp) >= 3 and len(set(tmp)) > 1:
            ans.append(' '.join(tmp[:-3]))
            tmp = tmp[-3:]
        else:
            ans.append(''.join(tmp))
            tmp = [c]
ans.append(''.join(tmp))
print(' '.join(ans))
