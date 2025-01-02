import sys,math,fractions,bisect
def fi():
    return int(sys.stdin.readline())

def fi2():
    return map(int, sys.stdin.readline().split())

def fi3():
    return sys.stdin.readline()

def fo(*args):
    for s in args:
        sys.stdout.write(str(s)+' ')
    sys.stdout.write('\n')
INF=2000000000
MOD=10**9+7
sys.setrecursionlimit(INF)

#main
n=fi()
ans=[[] for i in range(n)]

x=1
start=0
while x<=n**2:
    for i in range(start,start+n):
        ans[i%n].append(x)
        x+=1
    start+=1
for i in range(n):
    for j in range(n):
        ans[i][j]=str(ans[i][j])
for i in range(n):
    fo(" ".join(ans[i]))
        
        
    
    
           

                           
                

            
        

        
        
        
    
    
    
            




    
            


    

        
    
    
        
        
        
    
    
    
            
            
            
            
    
                
    
        
    

        
        
    


    
    
            
                
            
            
        
    
    
        
    
    
    
            

    
    



    
        
            
    
        
