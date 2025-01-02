n=input()
c=0
f1=1;f2=1;f3=1
m=10**9+7
for i in range(n):
  f1*=10;f2*=9;f3*=8
  f1%=m;f2%=m;f3%=m
print (f1-2*f2+f3)%m
  
