from sys import stdin
t=int(input())
for _ in range(t):
          n,k=map(int,stdin.readline().split())
          if n==k:
              print("YES")
              print(1)
              print(1)
          else:
                    if n+2>k*2:
                              print("YES")
                              print(2)
                              print(n-k+1,end=" ")
                              print(1)
                    else:
                              print("NO")