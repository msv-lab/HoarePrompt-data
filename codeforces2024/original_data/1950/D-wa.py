otvet=[bin(i)[2::]for i in range(2,10)]
for i in range(int(input())):
    number=int(input())
    if "1" in set(str(number)) and "0" in set(str(number)) and len(set(str(number)))==2:
        print("YES")
        continue
    flag=True
    while flag!=False:
        if number==1:
            flag=False
        else:
            for z in otvet:
                if number%int(z)==0:
                    number//=int(z)
                    break
                elif z==otvet[-1]:
                    flag=False
                    print("NO")
                    break
    if number==1:
        print("YES")