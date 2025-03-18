for _ in range(int(input())):
  n=int(input())
  s=input()
  t=input()
  a=b=0
  for i in range(n):
    a+=s[i]>t[i]
    b+=s[i]<t[i]
  print(max(a,b))