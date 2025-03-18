def solve(arr,n):
  ans=[10**9]*n
  i=n-2
  while i>=0:
    ans[i]=ans[i+1]-arr[i]
    i-=1
  return ans
 
 
t=int(input())
while t:
  n=int(input())
  arr=[int(x) for x in input().split(' ')]
  ans=solve(arr,n)
  for i in ans:
    print(i,end=' ')
  print()
  t-=1