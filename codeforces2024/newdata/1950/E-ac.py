from collections import defaultdict
def generate_factors(number):
    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:  
                factors.append(number // i)
    return sorted(factors)

for _ in range(int(input())):
    n=int(input())
    s=input()
    g=list(s)

    for i in range(len(generate_factors(n))):
        p=generate_factors(n)[i]
        diff=0
        mymap=defaultdict(int)
        for j in range(0,n,p):
            sb=g[j:j+p]
            result = ''.join(sb)
            mymap[result]+=1
        
        #print(mymap)
        if len(mymap)==1:
            diff=1
        elif len(mymap)==2 and min(mymap.values())==1:
            # print("ya")
            sl=[]
            for ele in mymap:
                sl.append(ele)
            
            s1,s2=list(sl[0]),list(sl[1])
            # print(s1,s2,len(s1),diff)
            for fd in range(len(s1)):
                if s1[fd]!=s2[fd]:
                    diff+=1
            # print(diff)
        else:
            diff=10

        if diff<2:
            ans=p
            break
    
    print(ans)