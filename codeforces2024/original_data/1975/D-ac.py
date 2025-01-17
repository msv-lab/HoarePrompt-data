t=int(input())
while t:
    t-=1
    n=int(input())
    a,b=map(int,input().split())
    adj_list=[[] for i in range(n+1)]
    for i in range(n-1):
        x,y=map(int,input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)
    answer1=0
    answer3=0
    store_prev=[0 for i in range(n+1)]
    store_prev[a]=a
    queue=[a]
    visited=[0 for i in range(n+1)]
    visited[a]=1
    level=0
    flag=0
    while queue:
        level+=1
        queue2=[]
        while queue:
            node=queue.pop()
            for i in adj_list[node]:
                if visited[i]==0:
                    visited[i]=1
                    store_prev[i]=node
                    if i==b:
                        flag=1
                        break
                    queue2.append(i)
            if flag==1:
                break
        if flag==1:
            break
        queue=queue2
    step=int((level+1)/2)
    answer1=step
    x=b
    if a==b:
        step=0
        answer1=0
    while step:
        x=store_prev[x]
        step-=1
    queue=[x]
    visited=[0 for i in range(n+1)]
    visited[x]=1
    level=0
    while queue:
        level+=1
        queue2=[]
        while queue:
            node=queue.pop()
            for i in adj_list[node]:
                if visited[i]==0:
                    visited[i]=1
                    queue2.append(i)
        queue=queue2
    answer3=level

    answer2=2*(n-1)
        
    
    print(answer2+answer1-answer3+1)