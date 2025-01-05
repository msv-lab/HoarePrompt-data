raw_input()
l=raw_input().split()
m=0
for i in l :
    s=0
    for j in i:
        if j.isupper() :
              s+=1
    m=max(s,m)
        
print(m)
        
