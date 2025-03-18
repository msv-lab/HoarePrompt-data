num=input()
out=[]
for numbers in range(int(num)):
    list2=[]
    list1=[]
    a=input()
    a=int(a)
    
    b=input("")
    list1=b.split()
    list1.sort()
    
    for i in range(a):
        list2.append(int(list1[2*i]))
        
 
    out.append(sum(list2))
    del list1[:]
    del list2[:]
    
    
 
for outputs in out:
    print(outputs)