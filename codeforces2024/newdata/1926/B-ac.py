for _ in range(int(input())):
    q=[]
    for i in range(int(input())):
        b=input()
        if '1'  in b:
            q.append(b)
    for j in range(len(q)-1):
        if q[j]!=q[j+1]:
            print('TRIANGLE')
            break
            
        else:
            print('SQUARE')
            break
