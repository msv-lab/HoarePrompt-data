#State of the program right berfore the function call: The function operates in an interactive environment where the graph is defined by the interactor. The graph is a complete undirected graph with n vertices, from which exactly (n - 2) edges have been removed. The function can make up to n queries to the interactor to find a Hamiltonian path. Each test case is defined by an integer n (2 ≤ n ≤ 10^5), and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop has finished executing all iterations, and for each test case, a Hamiltonian path has been constructed and printed in the format `! path`, where `path` is a space-separated list of integers representing the vertices in the Hamiltonian path. The variables `vx` and `ops` are reset for each new test case, and their final state is not retained between test cases.
#Overall this is what the function does:The function `func` operates in an interactive environment to find and print a Hamiltonian path in a graph with `n` vertices and `(n - 2)` removed edges. It processes multiple test cases, each defined by an integer `n` (2 ≤ n ≤ 10^5). For each test case, the function queries the interactor to construct the Hamiltonian path and prints it in the format `! path`, where `path` is a space-separated list of integers representing the vertices in the path. The function does not return any value. After processing all test cases, the function concludes, and the final state of the program is that all Hamiltonian paths have been printed for the given test cases.

