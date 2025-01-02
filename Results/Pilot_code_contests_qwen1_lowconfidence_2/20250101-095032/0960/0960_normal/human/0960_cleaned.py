(n, m, v) = map(int, raw_input().split())
if m < n - 1:
    print(-1)
    exit()
edges = [(i, i + 1) for i in xrange(n - 1)]
m = m - len(edges)
node1_nr = 1
while m > 0 and node1_nr < n:
    node2_nr = node1_nr + 2
    while m > 0 and node2_nr < n:
        edges.append((node1_nr, node2_nr))
        m -= 1
        node2_nr += 1
    node1_nr += 1
if m > 0:
    print(-1)
    exit()
translate = [i + 1 for i in xrange(n)]
(translate[v - 1], translate[1]) = (translate[1], translate[v - 1])
output = ['%d %d' % (translate[n1], translate[n2]) for (n1, n2) in edges]
print('\n'.join(output))