cases=int(input())
for i in range(cases):
    arr=[]
    lex=int(input())
    for j in range(2):
        if(lex<=26):
            arr.append(1)
            lex=lex-1
        elif(lex<52):
            arr.append(26)
            lex=lex-26
        else:
            arr.append(26)
            lex=lex-26    
    arr.append(lex)
    arr.sort()
    for k in range(3):
        print(chr(arr[k]+96), end='')