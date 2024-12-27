import Queue

num, m, t = [int(i) for i in raw_input().split(' ')]
edges = [[] for i in range(num + 1)]
for i in range(m):
    src, dst, weight = [int(i) for i in raw_input().split(' ')]
    edges[src].append((dst, weight))

res = [[(-1, ":(") for j in range(m)] for i in range(num)]
res[0][1] = (1, [1])
queue = Queue.PriorityQueue()

queue.put((1, 1, t, [1]))
while not queue.empty():
    cur = queue.get()
    if res[cur[0] - 1][cur[1] - 1][0] > cur[2]:
        continue
    else:
        res[cur[0] - 1][cur[1] - 1] = (cur[2], cur[3])

    nxt = [(edge[0], cur[1] + 1, cur[2] - edge[1], cur[3] + [edge[0]]) for edge in edges[cur[0]]]
    for n in nxt:
        if n[2] < 0:
            continue
        queue.put(n)
final = ()
for i in res[num - 1]:
    if i[0] >= 0:
        final = i

print(final[0] + 1)
print(' '.join([str(x) for x in final[1]]))
   	 		   	 					  	 			  	   	