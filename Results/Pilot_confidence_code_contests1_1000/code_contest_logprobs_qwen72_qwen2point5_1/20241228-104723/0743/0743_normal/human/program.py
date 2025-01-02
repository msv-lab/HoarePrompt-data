from sys import stdin

s, all = stdin.readline().strip(), []
lst, ans = [s[0], 1], 0

for i in s[1:]:
    if i != lst[0]:
        all.append(lst)
        lst = [i, 0]
    lst[-1] += 1

all.append(lst)
if (len(all) & 1):
    l = r = len(all) >> 1
    if all[r][1] >= 2:
        ans = all[r][1] + 1
        l -= 1
        r += 1
        while l > -1:
            if all[l][0] != all[r][0] or all[l][1] + all[r][1] < 3:
                ans = 0
                break

            l -= 1
            r += 1
print(ans)
