def main():
  #n = int(input())
  n, t = (int(i) for i in input().split())
  a = [[int(i) for i in input().split()] for i in range(n)]
  #b = [int(i) for i in input().split()]
  #c = [int(i) for i in input().split()]
  #s = input()
  #t = input()
  """q = int(input())
  while q:
    l, r = map(int, input().split())
    q -= 1
    """
  a.sort(key=lambda x: x[1])
  ans = 0
  l = r = 0
  res = 0
  while r<n:
    res += a[r][0]
    if r>0: res += a[r][1]-a[r-1][1]
    while res>t:
      res -= a[l][0]
      if l<n-1: res -= a[l+1][1]-a[l][1]
      l += 1
    ans = max(ans, r-l+1)
    r += 1
  return ans

t = int(input())
while t:
  print(main())
  t -= 1