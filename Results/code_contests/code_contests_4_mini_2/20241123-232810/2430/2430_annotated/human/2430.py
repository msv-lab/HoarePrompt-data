import sys
def ph(queue, n, nodes):
    HM = 2*26-1
    res = [0]*n
    while queue:
        #print queue[0]
        #print nodes
        cur = queue.pop(0)
        val = cur[1]
        ind = cur[0]
        res[ind] = val
        if val > HM:
            break
        val += 1
        
        for sosed in nodes[ind]:
            if res[sosed] == 0:
                queue.append([sosed, val])
                #print 'addd ' + str(sosed) + ' ' + str(val)
        
    if max(res) > HM:
        return "Impossible!"
    else:
        for ind in xrange(len(res)):
            val = res[ind]
            if val > 26:
                res[ind] = 2*26-val
        
        return ' '.join(map(lambda x: chr(26-x+ord('A')), res))

if True:
    n = int(sys.stdin.readline())
    edges = []
    for i in xrange(n-1):
        edges.append(map(lambda x: int(x)-1, sys.stdin.readline().split()))
    #print edges
else:
    n = 10
    edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]]

nodes = []
for i in xrange(n):
    nodes.append([])
#print edges

for edge in edges:
    #print edge[0], edge[1]
    nodes[edge[0]].append(edge[1])
    nodes[edge[1]].append(edge[0])

#print nodes
queue = []
for ind in xrange(len(nodes)):
    if len(nodes[ind]) == 1:
        queue.append([ind, 1])
print(ph(queue, n, nodes))
