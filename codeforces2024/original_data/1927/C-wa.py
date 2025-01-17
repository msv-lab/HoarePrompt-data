for iteration in range(int(input())):
    info=input().split(" ")
    row1=input().split(" ")
    row2=input().split(" ")
    duplicates=[]
    index1=[]
    index2=[]
    
    for i in range(0,len(row1)):
        temp=row1[i]
        if temp in row2:
            for i in range(len(row1)):
                if row1[i]==temp:
                    index1.append(i)
            for i in range(len(row2)):
                if row2[i]==temp:
                    index2.append(i)
            duplicates.append(temp)
        if int(temp)>int(info[2]):

            index1.append(i)

    for i in range(0,len(row2)):
                            
        if int(row2[i])>int(info[2]):
            index2.append(i)
    duplicates=set(duplicates)
    index1=set(index1)
    index2=set(index2)
    
    if (((len(row1)-len(index1))==(len(row2)-len(index2)) and len(duplicates)%2==0) or (len(row1)==len(row2)-len(index2)) or (len(row2)==len(row1)-len(index1))) and len(row1)+len(row2)+len(duplicates)-len(index1)-len(index2)==int(info[2]):
        print("YES")
    else:
        print("NO")

