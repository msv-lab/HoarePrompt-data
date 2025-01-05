#State of the program right berfore the function call: n is an integer representing the number of vertices (2 ≤ n ≤ 200,000), m is an integer representing the number of edges (n - 1 ≤ m ≤ min(200,000, (n(n-1))/2)), and D is an integer representing the required degree of the first vertex (1 ≤ D < n). The subsequent m lines contain pairs of integers (v_i, u_i) representing edges between vertices (1 ≤ v_i, u_i ≤ n, u_i ≠ v_i), and there are no self-loops or multiple edges.
def func():
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda : sys.stdin.readline().rstrip('\r\n')
    n, m, D = [int(x) for x in input().split(' ')]
    ds = defaultdict(set)
    dmain = defaultdict(set)
    for i in range(m):
        s, f = [int(x) for x in input().split(' ')]
        
        if s != 1 and f != 1:
            ds[s].add(f)
            ds[f].add(s)
        
        dmain[s].add(f)
        
        dmain[f].add(s)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is greater than or equal to 0, `D` is an integer, `ds` contains edges between vertices that are not 1, `dmain` contains all edges including those connected to vertex 1.
    if (len(dmain[1]) < D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n` is an integer, `m` is greater than or equal to 0, `D` is an integer, `ds` contains edges between vertices that are not 1, and `dmain` contains all edges including those connected to vertex 1. If the length of `dmain[1]` is less than `D`, 'NO' is printed and the program exits.
    arr = [0] * (n + 1)
    i = 2
    cur = 0
    while i < n:
        if arr[i] == 0:
            cur += 1
            tov = {i}
            arr[i] = cur
            while len(tov):
                nxt = tov.pop()
                for el in ds[nxt]:
                    if arr[el] == 0:
                        arr[el] = cur
                        tov.add(el)
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is `n`, `cur` is the number of distinct connected components found, `arr` has been updated such that each index reachable from the starting index 2 through the adjacency list `ds` has the same value as `cur`, and all other indices remain 0 if they were never reached.
    if (cur > D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`i` is `n`, `cur` is the number of distinct connected components found, `arr` has been updated such that each index reachable from the starting index 2 through the adjacency list `ds` has the same value as `cur`, and all other indices remain 0 if they were never reached. If `cur` is greater than `D`, 'NO' is printed and the program exits.
    sviaz = set()
    ite = dmain[1].copy()
    for el in ite:
        if arr[el] not in sviaz:
            sviaz.add(arr[el])
        else:
            dmain[el].remove(1)
            dmain[1].remove(el)
        
    #State of the program after the  for loop has been executed: `i` is `n`, `cur` is the number of distinct connected components found, `arr` has been updated, `sviaz` contains all distinct values from `arr` that were reachable from `ite`, `ite` is a copy of `dmain[1]` containing all elements that remained after removing those that were in `sviaz`, and `dmain[1]` has been updated accordingly.
    sv = set()
    sv.add(1)
    vis = set()
    vis.add(1)
    res = ['YES']
    while len(sv):
        nxt = sv.pop()
        
        for el in dmain[nxt]:
            if el not in vis:
                sv.add(el)
                vis.add(el)
                res.append(str(nxt) + ' ' + str(el))
            dmain[el].remove(nxt)
        
    #State of the program after the loop has been executed: `i` is `n`, `cur` is the number of distinct connected components found, `arr` has been updated, `sviaz` contains all distinct values from `arr` that were reachable from `ite`, `ite` is a copy of `dmain[1]`, `dmain[1]` has been updated accordingly, `sv` is empty, `vis` contains the value `1` and all elements that were added during the loop iterations, `res` is a list containing the strings 'YES' and all pairs in the format '<nxt> <el>' for every element added, and `dmain` has been updated such that all elements no longer contain any references to previously visited elements.
    print('\n'.join(res))
#Overall this is what the function does:The function analyzes a graph with `n` vertices and `m` edges to determine if the first vertex can achieve a degree of at least `D`. If the degree of vertex 1 is less than `D`, it prints 'NO' and exits. It also checks the number of distinct connected components in the graph, and if this number exceeds `D`, it again prints 'NO' and exits. If both conditions are satisfied, it constructs and prints a representation of the connections starting from vertex 1. If there are any vertices connected to vertex 1 that would create duplicates in the connections, those edges are removed accordingly before printing the result. The function ultimately returns 'YES' followed by the connections if the conditions are met.

