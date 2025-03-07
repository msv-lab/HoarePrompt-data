def solve(arr):
  i=0
  n=len(arr)
  j=len(arr)-1
  while i<len(arr)-1 and arr[i]==arr[i+1] :
      i+=1
  while j>0 and arr[j]==arr[j-1] :
      j-=1
  if arr[0]==arr[-1]:
     return max(j-i-1,0)
  return max(min(n-i-1,j),0)
 
t=int(input())
while t:
  n=int(input())
  arr=[int(x) for x in input().split(' ')]
  print(solve(arr))
  t-=1