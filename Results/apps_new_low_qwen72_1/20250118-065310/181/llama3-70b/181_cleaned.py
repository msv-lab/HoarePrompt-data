s = input()
k = int(input())
ans = []
i = 0
while i < len(s) and len(ans) < k:
    if s[i].isalpha():
        ans.append(s[i])
        if i + 1 < len(s) and s[i + 1] == '?':
            i += 2
        elif i + 1 < len(s) and s[i + 1] == '*':
            while i + 1 < len(s) and s[i + 1] == '*':
                ans.append(s[i])
                i += 2
            i += 1
        else:
            i += 1
    else:
        i += 1
if len(ans) == k:
    print(''.join(ans))
else:
    print('Impossible')