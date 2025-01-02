n,l=map(int,raw_input().split())
s=[raw_input() for _ in xrange(n)]
s.sort()
ans=""
for i in xrange(n):
    ans+=s[i]
print(ans)
