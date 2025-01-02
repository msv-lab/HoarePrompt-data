m, n=map(int,raw_input().split())

ll = map(int,raw_input().split())

sub = []
for i in range(0, n-1):
    sub.append(map(int,raw_input().split()))

result = 0
for s in sub:
    tmp = ll[s[0]-1:s[1]]
    a = sum(tmp)
    if a > 0:
        result += a

print(result)
