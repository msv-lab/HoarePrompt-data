from sys import stdin, stdout
n,m=map(int, stdin.readline().split())
arr=map(int, stdin.readline().split())
sums=[0]*(m+1)
l=0
res=[]
for i in xrange(m-1, -1, -1):
    sums[i]=sums[i+1]+arr[i]
for i in xrange(m):
    res.append(max(i, n-sums[i])+1)
stdout.write(' '.join(map(str, res)))