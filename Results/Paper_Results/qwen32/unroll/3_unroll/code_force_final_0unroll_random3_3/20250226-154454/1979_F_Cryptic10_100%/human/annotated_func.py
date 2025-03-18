#State of the program right berfore the function call: The function `func()` is designed to interactively determine a Hamiltonian path in a graph. The graph starts as a complete undirected graph with `n` vertices (2 ≤ n ≤ 10^5) and then has exactly (n - 2) edges removed. The function can make at most `n` queries of the form "? d" to gather information about the graph's structure, where `d` is an integer (0 ≤ d ≤ n - 1). The function should output a Hamiltonian path in the format "! v_1 v_2 ... v_n" after processing the queries. The sum of `n` across all test cases does not exceed 10^5.
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
        
    #State: the function `func()` will have interactively determined and printed a Hamiltonian path for each test case provided in the input. The state of variables not involved in the loop (such as the lambda function `q` and any external variables) remains unchanged.
#Overall this is what the function does:The function `func()` determines a Hamiltonian path in a graph through a series of queries. It starts with a complete undirected graph with `n` vertices and then removes exactly `n-2` edges. The function can make up to `n` queries to gather information about the graph's structure and outputs a Hamiltonian path in the format "! v_1 v_2 ... v_n" for each test case.

