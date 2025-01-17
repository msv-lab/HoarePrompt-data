p=int(input())
for i in range(p):
    n=int(input())
    s=input()
    lenght=len(s)

    if int(lenght)%2==0 and n%2==0:
        print(s[::-1]+s)
    else:
        print(s)    
