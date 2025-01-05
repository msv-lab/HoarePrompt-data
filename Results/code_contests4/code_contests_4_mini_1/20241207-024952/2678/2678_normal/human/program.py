# ANSHUL GAUTAM
# IIIT-D

'''

'''

def solve(grid):
	H,W = len(grid),len(grid[0])
	q = []
	dist = [0]*H
	for i in range(H):
		dist[i] = []
	for i in range(H):
		for j in range(W):
			if(grid[i][j] == '#'):
				q.append([i,j])
				grid[i][j] = 0
	maxx = 0
	while(q):
		qq = []
		for i,j in q:
			for r,c in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
				if(0 <= r < H and 0 <= c < W and grid[r][c] == '.'):
					grid[r][c] = grid[i][j] + 1
					maxx = max(maxx,grid[r][c])
					qq.append([r,c])
		q = qq
	return maxx

H,W = map(int, raw_input().split())
grid = []
for h in range(H):
	s = list(raw_input())
	grid.append(s)
ans = solve(grid)
print(ans)

