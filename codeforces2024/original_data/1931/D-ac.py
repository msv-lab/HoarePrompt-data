R=lambda:map(int,input().split())
t,=R()
while t:
 t-=1;n,x,y=R();d={};r=0
 for u in R():r+=d.get((-u%x,u%y),0);p=u%x,u%y;d[p]=d.get(p,0)+1
 print(r)