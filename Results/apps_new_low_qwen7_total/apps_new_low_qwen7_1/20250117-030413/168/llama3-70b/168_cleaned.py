a = input()
b = input()
i = 0
j = 0
ans = []
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        ans.append(a[i])
        i += 1
        j += 1
    else:
        i += 1
if len(ans) == 0:
    print('-')
else:
    print(''.join(ans))