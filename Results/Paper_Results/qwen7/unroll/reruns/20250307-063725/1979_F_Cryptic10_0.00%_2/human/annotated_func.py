#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph. The function is part of an interactive process where the graph is being queried to find a Hamiltonian path.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is an integer between 0 and n-1 inclusive)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two values, `v` and `u`, where `v` is an input integer and `u` is another input integer.
#Overall this is what the function does:The function accepts an integer `d` representing a vertex index in a graph with `n` vertices (where 0 <= d < n). It queries the graph to obtain the next vertex `v` in a Hamiltonian path starting from vertex `d`. After receiving `v`, it further queries the graph to get the subsequent vertex `u` in the path. The function then returns these two vertices `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5.
def func_2(n):
    path = []
    remaining_vertices = set(range(1, n + 1))
    while remaining_vertices:
        for d in range(n - 1, -1, -1):
            v, u = func_1(d)
            if v == 0:
                continue
            if v in remaining_vertices:
                path.append(v)
                remaining_vertices.remove(v)
                break
        
    #State: The `path` list contains some vertices from 1 to n, and `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [vertex1] [vertex2] ... [vertexN]
    sys.stdout.flush()
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 10^5) and constructs a path of vertices from 1 to n. It then prints the path as a sequence of vertices. The function ensures that all vertices from 1 to n are included in the path, and no vertex is repeated.

