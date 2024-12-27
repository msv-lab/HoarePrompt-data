from sys import stdin, stdout

n = int(stdin.readline())
a = [0] * n
a = map( int, stdin.readline().rstrip().split() )

res = 0
for i in range(1,n-1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        res +=1
    if a[i] < a[i+1] and a[i] < a[i-1]:
        res +=1

print(res)
