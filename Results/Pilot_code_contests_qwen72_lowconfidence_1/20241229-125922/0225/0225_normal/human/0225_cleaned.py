rstrs = lambda : [str(x) for x in stdin.readline().split()]
n = int(input())
(s, ans) = (sorted([rstrs() for _ in range(n)], key=lambda x: int(x[1])), [])
for i in range(n):
    if int(s[i][1]) > i:
        print(-1)
        exit()
    ans.insert(int(s[i][1]), ' '.join([s[i][0], str(n)]))
    n -= 1
print('\n'.join(ans))