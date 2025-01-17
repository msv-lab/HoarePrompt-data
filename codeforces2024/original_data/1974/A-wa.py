n=int(input())
d=15
f=14
for i in range(n):
      a,b=map(int,input().split())
      while a==0 and b==0:
            d=d-5
            a=a-1
            b=b-1
            f=f+1
            print(f)
