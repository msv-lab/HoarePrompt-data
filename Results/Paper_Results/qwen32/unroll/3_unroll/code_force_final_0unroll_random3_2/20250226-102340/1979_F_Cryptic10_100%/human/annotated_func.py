#State of the program right berfore the function call: The function `func()` does not take any input parameters. The interaction with the system is handled through standard input and output as described in the problem statement. Specifically, the function will receive multiple test cases, each starting with an integer `n` (2 ≤ n ≤ 10^5) representing the number of vertices in the graph. The function can then make up to `n` queries of the form "? d" (0 ≤ d ≤ n - 1) to gather information about the graph, and finally output a Hamiltonian path for each test case in the format "! v_1 v_2 ... v_n". The sum of `n` over all test cases does not exceed 10^5.
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
        
    #State: For each test case, the function will output a Hamiltonian path in the format "! v_1 v_2 ... v_n" after processing the graph using the specified queries and operations. The state of variables not directly involved in the loop, such as the lambda function `q`, remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases from standard input, where each test case consists of a graph with `n` vertices. For each graph, it interacts with an external system by making queries to gather information about the graph's structure. Based on the gathered information, it constructs and outputs a Hamiltonian path for the graph in the format "! v_1 v_2 ... v_n". The function does not accept any direct input parameters and its final state is characterized by having outputted a Hamiltonian path for each test case.

