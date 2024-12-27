from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
rstr = lambda: list(stdin.readline().strip())

n, s, a, ans = int(input()), rstr(), rints(), []

for i in range(n):
    hash, val = a[int(s[i]) - 1], int(s[i])
    if hash > val:
        ans.append(str(hash))

    elif hash == val:
        if ans:
            ans.append(str(hash))
        else:
            ans.append(s[i])
    else:
        if ans:
            break
        else:
            ans.append(s[i])

print(''.join(ans) + ''.join(s[len(ans):]))
