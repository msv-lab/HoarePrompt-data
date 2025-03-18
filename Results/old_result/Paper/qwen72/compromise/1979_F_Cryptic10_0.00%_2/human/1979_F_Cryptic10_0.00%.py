import sys
 
def query(d):
    print(f"? {d}")
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
 
def solve(n):
    path = []
    remaining_vertices = set(range(1, n + 1))
    
    while remaining_vertices:
        for d in range(n - 1, -1, -1):
            v, u = query(d)
            if v == 0:
                continue
            if v in remaining_vertices:
                path.append(v)
                remaining_vertices.remove(v)
                break
    
    print(f"! {' '.join(map(str, path))}")
    sys.stdout.flush()
 
t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)