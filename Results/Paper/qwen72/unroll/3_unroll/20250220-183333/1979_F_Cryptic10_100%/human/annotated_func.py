#State of the program right berfore the function call: The function operates in an interactive environment where the graph is modified based on queries. The graph is initially a complete undirected graph with n vertices, from which exactly (n - 2) edges have been removed. The function can make up to n queries of the form "? d" where d is an integer such that 0 <= d <= n - 1. The function must output a Hamiltonian path in the form "! v_1 v_2 ... v_n" where v_i are the vertices in the order of their occurrence in the path. The function must handle multiple test cases, with the number of test cases t satisfying 1 <= t <= 1000, and the number of vertices n in each test case satisfying 2 <= n <= 10^5. The sum of n over all test cases does not exceed 10^5.
def func():
    q = lambda d: print('? %d' % d, flush=True) or map(int, input().split())
    for _ in range(int(input())):
        vx, ops = set(i for i in range(1, int(input()) + 1)), []
        
        while len(vx) > 2:
            v1, v2 = q(len(vx) - 2)
            vx.remove(v1)
            if v2 > 0:
                ops += [(v1, v2)]
            else:
                v3, _ = q(0)
                vx.remove(v3)
                ops += [(v3, 0), (v1, 0)]
        
        p1, p2 = list(vx), []
        
        for v1, v2 in ops[::-1]:
            (p2 if p1[-1] == v2 else p1).append(v1)
        
        print('! %s' % ' '.join(map(str, p1[::-1] + p2)), flush=True)
        
    #State: The loop has processed all test cases. For each test case, it has printed the final sequence of vertices in the format "! vertex1 vertex2 ...", where the vertices are ordered such that any vertex v1 that has a direct edge to v2 (as determined by the queries) appears before v2 in the sequence. The variables `t` and `n` remain unchanged, and the function `q` continues to perform the same operations as initially defined.
#Overall this is what the function does:The function `func` operates in an interactive environment to handle multiple test cases. For each test case, it processes a complete undirected graph with `n` vertices, from which exactly `(n - 2)` edges have been removed. The function makes up to `n` queries to determine the structure of the graph, and then outputs a Hamiltonian path for the graph in the format "! v_1 v_2 ... v_n", where `v_i` are the vertices in the order of their occurrence in the path. After processing all test cases, the function has printed the Hamiltonian paths for each graph, and the variables `t` and `n` remain unchanged. The function `q` continues to perform the same operations as initially defined.

