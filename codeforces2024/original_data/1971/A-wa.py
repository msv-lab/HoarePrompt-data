def min(a,b):
    if a<b:
        return (a,b)
    elif a>b:
        return (b,a)
    

t = int(input())

for i in range (t):
    a,b = map(int,input().split())
    print(min(a,b))