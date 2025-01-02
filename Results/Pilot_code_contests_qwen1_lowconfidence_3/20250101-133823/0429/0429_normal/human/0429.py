# Python program for Dijkstra's 
# single source shortest 
# path algorithm. The program 
# is for adjacency matrix 
ans=[]
p=[]
# representation of the graph 

from collections import defaultdict 
pa=[]
#Class to represent a graph 
class Graph: 

	# A utility function to find the 
	# vertex with minimum dist value, from 
	# the set of vertices still in queue 
	def minDistance(self,dist,queue): 
		# Initialize min value and min_index as -1 
		minimum = float("Inf") 
		min_index = -1
		
		# from the dist array,pick one which 
		# has min value and is till in queue 
		for i in range(len(dist)): 
			if dist[i] < minimum and i in queue: 
				minimum = dist[i] 
				min_index = i 
		return min_index 


	# Function to print shortest path 
	# from source to j 
	# using parent array 
	def printPath(self, parent, j): 
		global p
		global pa 
		#Base Case : If j is source 
		if parent[j] == -1 : 
		#	print j, 
			p.append(j)
			pa.append(p)
			return
		self.printPath(parent , parent[j]) 
		#print j, 
		p.append(j)
        
	# A utility function to print 
	# the constructed distance 
	# array 
	def printSolution(self, dist, parent): 
		src = 0
		global p
	#	print("Vertex \t\tDistance from Source\tPath") 
		for i in range(1, len(dist)): 
		#	print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])), 
			p=[]
			self.printPath(parent,i) 
			#print(p,'fun')
		#	pa.append(p)

	'''Function that implements Dijkstra's single source shortest path 
	algorithm for a graph represented using adjacency matrix 
	representation'''
	def dijkstra(self, graph, src): 

		row = len(graph) 
		col = len(graph[0]) 

		# The output array. dist[i] will hold 
		# the shortest distance from src to i 
		# Initialize all distances as INFINITE 
		dist = [float("Inf")] * row 

		#Parent array to store 
		# shortest path tree 
		parent = [-1] * row 

		# Distance of source vertex 
		# from itself is always 0 
		dist[src] = 0
	
		# Add all vertices in queue 
		queue = [] 
		for i in range(row): 
			queue.append(i) 
			
		#Find shortest path for all vertices 
		while queue: 

			# Pick the minimum dist vertex 
			# from the set of vertices 
			# still in queue 
			u = self.minDistance(dist,queue) 

			# remove min element	 
			queue.remove(u) 

			# Update dist value and parent 
			# index of the adjacent vertices of 
			# the picked vertex. Consider only 
			# those vertices which are still in 
			# queue 
			for i in range(col): 
				'''Update dist[i] only if it is in queue, there is 
				an edge from u to i, and total weight of path from 
				src to i through u is smaller than current value of 
				dist[i]'''
				if graph[u][i] and i in queue: 
					if dist[u] + graph[u][i] < dist[i]: 
						dist[i] = dist[u] + graph[u][i] 
						parent[i] = u 


		# print the constructed distance array 
		self.printSolution(dist,parent) 

g= Graph() 
edge=[]
n,m=map(int,raw_input().split())
graph=[[0 for j in range(n)]for i in range(n)]
for i in range(m):
    a,b,c=map(int,raw_input().split())
    a,b=min(a,b),max(a,b)
    edge.append([a-1,b-1])
    graph[a-1][b-1]=c 
    graph[b-1][a-1]=c 

		

ans={}
for i in range(n):
    p=[]
    g.dijkstra(graph,i) 
   # print(p)
    for i in range(len(p)-1):
        a,b=p[i],p[i+1]
        a,b=min(a,b),max(a,b)
        ans[(a,b)]=1 
#print(ans)
#print(pa)
# This code is contributed by Neelam Yadav 
cnt=0 
for i in edge: 
    if ans.get((i[0],i[1]),-1)!=-1:
        cnt+=1 
print(m-cnt)