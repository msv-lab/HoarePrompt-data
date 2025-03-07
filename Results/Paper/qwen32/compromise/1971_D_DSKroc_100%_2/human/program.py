import math
t = int(input())
for q in range(t) :
    s =  input()
    count=0
    flag = 0
    for i in range(len(s)-1) :
        if int(s[i]) != int(s[i+1]) :
            count+=1
        if int(s[i]) < int(s[i+1]): flag =1
    if flag==0 :print(count+1)
    else : print(count)