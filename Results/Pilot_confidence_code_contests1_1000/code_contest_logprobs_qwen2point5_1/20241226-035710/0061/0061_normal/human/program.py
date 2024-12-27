a = raw_input()
#print type(a)
list=[]
list1=[]
list2=[]
for i in a:
    list.append(i)
for j in range(len(list)):
    if (j+1)%2==1:
        list1.append(list[j])
        list1.sort()
        a=len(list1)
#print a

for i in range(len(list1)):
    list2.append(list1[i])
    if a>1:
        list2.append("+")
print(''.join(map(str, list2[:-1])))
