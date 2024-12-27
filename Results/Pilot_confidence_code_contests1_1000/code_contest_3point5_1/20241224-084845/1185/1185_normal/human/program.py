n, q =  map(int, raw_input().split())
graph = dict()
operation = [0 for i in range(q)]
for i in range(n-1):
    a, b = map(int, raw_input().split())
    if a in graph.keys():
        graph[a].add(b)
    else:
        graph[a] = set([b])
    if b in graph.keys():
        graph[b].add(a)
    else:
        graph[b] = set([a])

for i in range(q):
    operation[i] = [int(j) for j in raw_input().split()]

values = [0 for i in range(n)]

vertex_list = dict()
for i in range(1, n+1):
    vertex_list[i] = set([-1])

def obtain_list(graphx, vertex, check, root):
    check[vertex-1] = True
    vertex_list[root].add(vertex)
    for v in graph[vertex]:
        if check[v - 1] == True:
            continue
        obtain_list(graphx, v, check, root)



# def dfs(graphx, vertex, check, value):
    # check[vertex-1] = True
    # values[vertex-1] += value
    # for v in graph[vertex]:
    #     if check[v - 1] == True:
    #         continue
    #     dfs(graphx, v, check, value)


# for i in range(q):
    # check_list = [False for j in range(n)]
    # ver = operation[i][0]
    # for v in graph[ver]:
    #     if v < ver:
    #         check_list[v-1] = True
    # dfs(graph, operation[i][0], check_list, operation[i][1])

for i in range(1, n+1):
    check_list = [False for j in range(n)]
    for v in graph[i]:
        if v < i:
            check_list[v-1] = True
    obtain_list(graph, i, check_list, i)


for i in range(q):
    p = operation[i][0]
    x = operation[i][1]
    for y in vertex_list[p]:
        if y != -1:
            values[y-1] += x

mapped_values = map(str, values)

result = ""
for i in range(n):
    result += mapped_values[i]
    if i < n - 1:
        result += " "

print(result)

