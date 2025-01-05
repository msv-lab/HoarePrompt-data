import math 
n,r=map(int,raw_input().split())
pi=3.1415926535897932384626433832795
ans=float((n*r*r*math.sin(pi/(2*n))*math.sin(pi/n))/math.sin((3*pi)/(2*n)))
print(ans);
