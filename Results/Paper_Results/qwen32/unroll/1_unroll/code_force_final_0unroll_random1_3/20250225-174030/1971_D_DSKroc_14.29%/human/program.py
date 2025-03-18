import math
t = int(input())
for q in range(t) :
    s =  input()
    count=0
    for i in range(len(s)-1) :
        if int(s[i]) > int(s[i+1]) :
            count+=1
    print(count+1)