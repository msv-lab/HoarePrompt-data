#State of the program right berfore the function call: The function operates in an interactive environment where the input is provided through a series of queries and responses. The input consists of multiple test cases, each with a single integer n (2 ≤ n ≤ 10^5) representing the number of vertices in a complete undirected graph from which (n - 2) edges have been removed. The function can make at most n queries of the form "? d" (0 ≤ d ≤ n - 1) to the interactor, and must output a Hamiltonian path for each test case. The interactor is non-adaptive, meaning the graph does not change during the interaction.
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
        
    #State: `vx` is a set containing exactly 2 integers, `ops` is an empty list, `p1` is a list containing the two integers from `vx` and all `v1` values from `ops` tuples where `p1[-1]` was not equal to `v2`, `p2` is a list containing all `v1` values from `ops` tuples where `p1[-1]` was equal to `v2`.
#Overall this is what the function does:The function `func` operates in an interactive environment to handle multiple test cases, each involving a complete undirected graph with `n` vertices and (n - 2) edges removed. It queries the interactor to determine the structure of the graph and constructs a Hamiltonian path for each test case. After processing all test cases, the function outputs the Hamiltonian paths, and the final state of the program is that `vx` is a set containing exactly 2 integers, `ops` is an empty list, `p1` is a list containing the two integers from `vx` and all `v1` values from `ops` tuples where `p1[-1]` was not equal to `v2`, and `p2` is a list containing all `v1` values from `ops` tuples where `p1[-1]` was equal to `v2`.

