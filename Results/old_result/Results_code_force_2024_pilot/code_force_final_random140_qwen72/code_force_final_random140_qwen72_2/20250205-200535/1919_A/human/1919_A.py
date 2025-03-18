t = int(input())
 
for _rep in range(t):
  n, k = list(map(int, input().split()))
 
  if n > k:
    print("Bob")
  elif n < k:
    print("Alice")
  else:
    print("Bob")