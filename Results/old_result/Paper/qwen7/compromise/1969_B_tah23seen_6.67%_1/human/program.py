def solve(sChar):
  s=[]
  for i in sChar:
    s.append(i)
 
  left=0
  cost=0
  right=1
  while left<=right and right<len(s) and left<len(s):
    if s[right]=='0' and s[left]=='1':
      s[right],s[left]=s[left],s[right]
      cost+=(right-left)+1
    while right<len(s) and s[right]!='0':
      right+=1
    while left<len(s) and  s[left]!='1':
      left+=1
  return cost
 
t=int(input())
while t:
  s=input()
  print(solve(s))
  t=t-1