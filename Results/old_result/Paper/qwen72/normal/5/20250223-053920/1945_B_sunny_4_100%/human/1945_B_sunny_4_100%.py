'''t=int(input())
for _ in range(t):
    a,b,m=map(int,input().split())
    A=int(m/a)+1
    B=int(m/b)+1
    print(A+B)'''
t = int(input())
for qi in range(t):
    a, b, m = [int(x) for x in  input().split()]
    ans = m // a + m // b + 2
    print(ans)