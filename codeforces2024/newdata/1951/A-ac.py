for i in range(int(input())):
  n=int(input())
  s=input()
  count=s.count('1')
  if count%2:
    print('NO')
  else:
    if count==2 and '11' in s:
      print('NO')
    else:
      print('YES')
