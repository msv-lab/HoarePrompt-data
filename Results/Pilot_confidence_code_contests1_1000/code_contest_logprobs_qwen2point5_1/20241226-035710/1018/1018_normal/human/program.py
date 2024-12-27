def bfs1(graph, root):
    count=-1
    visited = [False for i in range(n+1)]
    queue=[None,root]
    visited[root]=True
    prob=[0 for i in range(n+1)]
    prob[1]=1
    ans=0
    while queue!=0:
        vertex = queue.pop(0)
        if vertex!=None and len(graph[vertex])==1 and visited[vertex]:
            ans+=leaf[vertex]/prob[vertex]
        if vertex is None:
            count+=1
            queue.append(None)
            if len(queue)==1:
                break
            else:
                continue
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                if leaf[neighbour]==1:
                    leaf[neighbour]=(count+1)
                if vertex==1:
                    prob[neighbour]=(prob[vertex]*(len(graph[vertex])))
                else:
                    prob[neighbour]=(prob[vertex]*(len(graph[vertex])-1))
                visited[neighbour]=True
                queue.append(neighbour)
    return(ans)
n=int(raw_input())
graph=[[] for i in range(n+1)]
for i in range(n-1):
    one,two=map(int,raw_input().split())
    graph[one].append(two)
    graph[two].append(one)
leaf=[0 for i in range(n+1)]
for i in range(len(graph)):
    if len(graph[i])==1 and i!=1:
        leaf[i]=1
leaf1=(bfs1(graph,1))
print(leaf1)
