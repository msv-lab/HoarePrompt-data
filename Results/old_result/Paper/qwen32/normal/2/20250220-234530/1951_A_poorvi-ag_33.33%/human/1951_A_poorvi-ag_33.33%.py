from collections import Counter
t=int(input())
results=[]
 
for i in range(t):
    n=int(input())
    arr=input()
    if arr.count('1')==2 and (('11') in arr):
        results.append('no')
    if arr.count('1')%2==0:
        if arr.count('1')==2 and (('11') in arr):
            results.append('no')
        
        else:results.append('yes')
    else: results.append('no')
    
for r in results:
    print(r)