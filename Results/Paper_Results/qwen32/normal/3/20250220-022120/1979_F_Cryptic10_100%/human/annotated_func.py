#State of the program right berfore the function call: The function `func()` does not take any input parameters. The input for the function is provided interactively through standard input, where the first line contains a single integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case starts with a single integer n (2 ≤ n ≤ 10^5) representing the number of vertices in the graph. The sum of n over all test cases does not exceed 10^5. The function must interact with the interactor by making queries of the form "? d" (0 ≤ d ≤ n - 1) and receiving responses, and finally output the Hamiltonian path in the format "! v_1 v_2 ... v_n".
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
        
    #State: `vx` is an empty set, `ops` is an empty list, `p1` and `p2` are lists forming the Hamiltonian path for the current test case, and the Hamiltonian path is printed for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case describes a graph. For each graph, it interacts with an interactor to determine a Hamiltonian path and then outputs the path in the specified format.

