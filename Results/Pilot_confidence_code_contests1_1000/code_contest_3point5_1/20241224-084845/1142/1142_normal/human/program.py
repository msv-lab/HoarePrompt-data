N = int(raw_input())
d = map(int, raw_input().split())

sum1 = 0
for i in range(N):
    sum1 = sum1 + d[i]

sum1 = sum1*sum1

sum2 = 0
for i in range(N):
    sum2 = sum2 + d[i]**2

print (sum1 - sum2)/2