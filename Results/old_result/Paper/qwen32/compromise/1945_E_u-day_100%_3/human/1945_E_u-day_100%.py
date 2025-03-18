def inp(): return map(int, input().split())
def linp(): return list(inp())
 
def solve():
  n, k = inp()
  arr = linp()
  
  pos = -1
  for i in range(n):
    if arr[i] == k:
      pos = i
  
  low, high = 0, n
  st = set()
  
  while low+1 < high:
    mid = (low + high)//2
    st.add(mid)
    
    if arr[mid] > k:
      high = mid
    else:
      low = mid
  
  if arr[low] == k:
    print(0)
  else:
    print(1)
    print(low+1, pos+1)
      
 
for _ in range(int(input())):
  solve()