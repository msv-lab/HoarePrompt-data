cases=int(input())
info=[]
for i in range(cases):
    arr=[]
    lex=int(input())
    for j in range(2):
        if(lex<28):
            arr.append(1)
            lex=lex-1
        elif(lex<52):
            arr.append(26)
            lex=lex-26
        elif(lex<=78):
            arr.append(26)
            lex=lex-26
    arr.append(lex)
    arr.sort()
    info.append(arr)
for i in range(cases):
    temp=''
    for j in range(3):
        temp=temp+chr(info[i][j]+96)
    print(temp)