n,m,k=map(int,raw_input().split())
l=[[0 for j in range(m)] for i in range(n)]
"""for i in range(n):
        for j in range(m):
            print l[i][j],
        print"""
while k>0:
    k-=1
    a,b,c=map(int,raw_input().split())
    if a==1:
        for i in range(m):
            l[b-1][i]=c
    else:
        for i in range(n):
            l[i][b-1]=c

print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in l]))