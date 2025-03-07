from collections import Counter
t=int(input())
results=[]
for i in range(t):
    n=int(input())
    arr=input()
    
    if arr.count('U')%2==1: results.append("yes")
    else: results.append("no")
    
for i in results:
    print(i)