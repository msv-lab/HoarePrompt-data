for _ in range(int(input())):
  n=int(input())
  s=input()
  d=0
  for i in range(len(s)):
    if(s[i]=='@'):
      d+=1
    if(s[i-1]=='*' and s[i]=='*'):
      break
  print(d)