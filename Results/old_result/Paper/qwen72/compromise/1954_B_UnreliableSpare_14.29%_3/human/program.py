# "Dread it, run from it, destiny arrives all the same" ~  Thanos
import copy, math, random, decimal
from decimal import Decimal
 
def solve():
  n = int(input())
  arr = list(map(int, input().split()))
 
  flag = True 
  for i in range(1,n):
    if arr[i] != arr[i-1]:
      flag = False 
      break 
 
  ans = Decimal("Infinity")
  val, cnt = arr[0], 0
  for i in range(n):
    if arr[i] == val:
      cnt += 1
    else:
      ans = min(ans, cnt)
  ans = min(ans, cnt)
 
  if flag: print(-1)
  else: print(ans)
 
 
if __name__ == "__main__":
  for _ in range(int(input())):
    solve()
  # solve()