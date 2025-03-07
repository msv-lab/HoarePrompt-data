n=input()
final=[]
for num in range(int(n)):
    s=0
    list2=[]
    a=input()
    list1=[]
    b=input()
    list1=b.split()
    for str in list1:
        list2.append(int(str))
 
    list2.sort()
    for i in range(0,len(list2),2):
        s=s+int(list2[i])
 
 
    final.append(s)
 
for fin in final:
    print(fin)