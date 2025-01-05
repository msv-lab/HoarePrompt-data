import sys

n = int(sys.stdin.readline())
start = [int(x) for x in sys.stdin.readline().split()]
end = [int(x) for x in sys.stdin.readline().split()]

start_m = {}
for index, val in enumerate(start):
    start_m[val] = index

end_m = {}
for index, val in enumerate(end):
    end_m[val] = index

res = 0
for v1, i1 in start_m.items():
    i2 = end_m[v1]
    n_moves = i2 - i1
    if n_moves < 0:
        n_moves = n - i1
    res = max(res, n_moves)
    
print(res)
    
