a,b,c = map(float,raw_input().split())
#a = (input()).spl
#b = float(input())
#c = float(input())
x = ((a/b)*c)**0.5
y = (b/c*a)**0.5
z = (c/a*b)**0.5
print (4*(x+y+z))