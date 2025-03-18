for ii in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  a.sort()
  r = a[0]
  rem = 0
  y=0
  for i in range(0,n-1):
    if (i+1)*(a[i+1]-a[i]) > k:
      r = a[i] + k//(i+1)
      rem = k%(i+1)
      y=n-1-i
      k=0
      break
    else:
      k-=(i+1)*(a[i+1]-a[i])
      r = a[i+1]
  if k!=0:
    r = a[n-1]+k//(n)
    print((r-1)*n +1)
  else:
    print((r-1)*n+1+rem+y)