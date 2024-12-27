N, X = map(int, raw_input().split())
x = map(int, raw_input().split())

size = len(x)

sum = 0

for i in range(size-1):
  sum = sum + (x[size-1-i]-x[size-2-i])*(i+2)*(i+2)+X
  
sum = sum + x[size-1] + x[0]*(N+1)*(N+1) + X*2

sum1 = 0
for i in range(size):
  sum1 = sum1 + x[i]*5
  
sum1 = sum1 + (N-1)*2*X
  
print(min(sum, sum1))
  
  