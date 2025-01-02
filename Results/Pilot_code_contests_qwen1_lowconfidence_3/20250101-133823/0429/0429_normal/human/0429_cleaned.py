ans = []
p = []
pa = []

class Graph:

    def minDistance(self, dist, queue):
        minimum = float('Inf')
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        global p
        global pa
        if parent[j] == -1:
            p.append(j)
            pa.append(p)
            return
        self.printPath(parent, parent[j])
        p.append(j)

    def printSolution(self, dist, parent):
        src = 0
        global p
        for i in range(1, len(dist)):
            p = []
            self.printPath(parent, i)
    "Function that implements Dijkstra's single source shortest path \n\talgorithm for a graph represented using adjacency matrix \n\trepresentation"

    def dijkstra(self, graph, src):
        row = len(graph)
        col = len(graph[0])
        dist = [float('Inf')] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                'Update dist[i] only if it is in queue, there is \n\t\t\t\tan edge from u to i, and total weight of path from \n\t\t\t\tsrc to i through u is smaller than current value of \n\t\t\t\tdist[i]'
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        self.printSolution(dist, parent)
g = Graph()
edge = []
(n, m) = map(int, raw_input().split())
graph = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    (a, b, c) = map(int, raw_input().split())
    (a, b) = (min(a, b), max(a, b))
    edge.append([a - 1, b - 1])
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
ans = {}
for i in range(n):
    p = []
    g.dijkstra(graph, i)
    for i in range(len(p) - 1):
        (a, b) = (p[i], p[i + 1])
        (a, b) = (min(a, b), max(a, b))
        ans[a, b] = 1
cnt = 0
for i in edge:
    if ans.get((i[0], i[1]), -1) != -1:
        cnt += 1
print(m - cnt)