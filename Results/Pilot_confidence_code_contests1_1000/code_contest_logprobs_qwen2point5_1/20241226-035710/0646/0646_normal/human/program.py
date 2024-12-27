n, m = map(int, raw_input().split())
rev_ans = []
par = {i: i for i in range(1, n + 1)}
size = {i: 1 for i in range(1, n + 1)}
input_ab = []


def root(_i):
    if par[_i] == _i:
        return _i
    else:
        return root(par[_i])


for i in range(m):
    input_ab.append(raw_input())

count = (n * (n - 1)) / 2
for ab in reversed(input_ab):

    rev_ans.append(count)
    a, b = map(int, ab.split())
    ra = root(a)
    rb = root(b)
    if ra != rb:
        sa = size[ra]
        sb = size[rb]
        count -= sa * sb
        par[rb] = ra
        size[ra] += sb

for i in reversed(rev_ans):
    print(i)

