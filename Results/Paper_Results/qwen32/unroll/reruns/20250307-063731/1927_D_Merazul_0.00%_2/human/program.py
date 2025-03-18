R=lambda:map(int,input().split())
t,=R()
while t:
 t-=1;*_,k=R();a={*R()};b={*R()};f=1;m=n=k//2
 for i in range(1,k+1):u=i in a;v=i in b;f&=u|v;m-=u&~v;n-=~u&v
 print('YNEOS'[f^1or m|n<0::2])