import heapq
from collections import defaultdict

def main():
  n = int(input())
  adj = defaultdict(set)
  for i in range(n-1):
    fro, to = [int(x) for x in input().split()]
    adj[fro].add(to)
    adj[to].add(fro)
    
  # print(adj)
  pq = []
  for node in adj:
    if len(adj[node]) == 1:
      heapq.heappush(pq, (1, node))
  # print(pq)
      
  sizes = {i: 1 for i in range(1, n+1)}
  
  while len(pq) > 1:
    ants, node = heapq.heappop(pq)
    # print("processing", node)
    # print(sizes)
    
    neighboring = adj[node]
    # print(node, neighboring)
    assert len(neighboring) == 1
    neighbor = list(neighboring)[0]
    
    if sizes[neighbor] < ants:
      print("NO")
      return
    
    adj[neighbor].remove(node)
    
    newSize = ants + sizes[neighbor]
    sizes[neighbor] = newSize
    
    if len(adj[neighbor]) == 1:
      # print(sizes[neighbor])
      heapq.heappush(pq, (newSize, neighbor))
    # print(sizes)
  
  print("YES")
    

  

  
if __name__ == "__main__":
  main()