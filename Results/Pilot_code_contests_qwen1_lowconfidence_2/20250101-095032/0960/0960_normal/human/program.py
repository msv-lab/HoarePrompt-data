#!/usr/bin/env python

(n,m,v) = map(int, raw_input().split())

if (m < (n-1)):
  print(-1)
  exit()

# Were going to make node 0 lose connection with the rest of the network,
# when node 1 fails. Put all nodes > 1 on the other side of 1 results in
# the largest possible network.

# Make a line
edges = [(i, i+1) for i in xrange(n-1)]

# Keep adding edges until the requested amount is reached (if possible)
m = m - len(edges)
node1_nr = 1
while ((m > 0) and (node1_nr < n)):
  node2_nr = node1_nr + 2 # Edge from node1_nr to node1_nr+1 already exists
  while ((m > 0) and (node2_nr < n)):
    edges.append((node1_nr, node2_nr))
    m -= 1
    node2_nr += 1
  node1_nr += 1

if (m > 0):
  # Unable to make the requested amount of edges
  print(-1)
  exit()

# Make a translation table
translate = [i+1 for i in xrange(n)]
translate[v-1],translate[1] = translate[1],translate[v-1] # Swap v and 1

# Construct output
output = [("%d %d" % (translate[n1], translate[n2])) for (n1, n2) in edges]
print("\n".join(output))
