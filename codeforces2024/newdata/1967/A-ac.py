import sys


cnt = 0
t=0
n = [0]
k = [0]
a = [0]
curt = 0
for line in sys.stdin:
    numbers = [int(x) for x in line.strip().split()]
    if(len(numbers) == 0):
        break
   
    if(cnt == 0):      
        t = numbers[0]
        n = [0 for col in range(t)]
        k = [0 for col in range(t)]
        a = [0 for row in range(t)]
        pref = [0 for row in range(t)]

    if(cnt%2 ==1 ):
           n[curt] = numbers[0]
           k[curt] = numbers[1]
           curt+=1
           
    if(cnt%2 == 0 and cnt > 0):

        a[curt-1] = sorted(numbers)
        pref[curt-1] = [0]*len(numbers)
        pref[curt-1][0] = a[curt-1][0]
        for i in range(1,len(numbers)):
            pref[curt-1][i] = pref[curt-1][i-1] + a[curt-1][i]
     
    cnt+=1
 
def check(goal,a,k,t):
    tot = 0
    lim1 = 0
    lim2 = len(a)-1
    
    flag = 1
    while(flag):
        #print(lim1,lim2)
        mid = (lim1+lim2)//2
        if(goal>= a[mid]):
            lim1 = mid
        else:
            lim2 = mid-1
        if(lim1 == lim2):
            flag = 0
        if(lim1 +1 >= lim2):
            if(goal>= a[lim2]):
                lim1 = lim2
            flag = 0
    tot = (lim1 + 1)*goal - pref[t][lim1]
    #print(lim1,goal,a,tot,k, pref[t])
    if(tot <=k):
        return 1,k-tot
    else:
        return 0,k-tot





 

for i in range(t):
    ans = 0
    e = max(a[i])
    lim2 = max(a[i]) + k[i]
    lim1 = min(a[i])
    flag = 1
    flgg = 0
    while (flag):
        
        mid = (lim2+lim1)//2
        #print(lim1,mid,lim2, "a")

        if(check(mid,a[i],k[i],i)[0]):

            lim1 = mid
        else:
            lim2 = mid
            
        #print(lim1,mid,lim2, "b")                 
        if(lim1+1 >= lim2):
            if(check(lim2,a[i],k[i],i)[0]):
                lim1 = lim2
            flag = 0
            
    ans = (lim1-1)*n[i]+1    + check(lim1,a[i],k[i],i)[1]
    for j in range(n[i]):
        if(a[i][j]>= lim1+1):
            ans+=1    
    print(ans)


    
   
    
 
    
    