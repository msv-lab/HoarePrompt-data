#State of the program right berfore the function call: The function `func` is intended to interact with a predefined interactor that manages the graph and responses. The graph is a complete undirected graph with `n` vertices, from which exactly `(n - 2)` edges have been removed. The function must handle multiple test cases, where the number of test cases `t` satisfies \(1 \le t \le 1000\), and for each test case, `n` satisfies \(2 \le n \le 10^5\). The sum of `n` over all test cases does not exceed \(10^5\). The function can make up to `n` queries of the form "? d" to the interactor, where `d` is an integer such that \(0 \le d \le n - 1\). The interactor responds with two integers representing a vertex and another vertex not connected to it, or "0 0" if no such vertex exists. The function must output a Hamiltonian path in the form "! v_1 v_2 ... v_n" and flush the output buffer after each query and answer.
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
        
    #State: The loop has processed all test cases. For each test case, `vx` is a set containing exactly 2 integers from the original set of integers from 1 to `n` inclusive, where `n` is the number of vertices in the graph for that test case. `ops` is a list of tuples representing the operations performed during the loop for that test case. `p1` is a list containing the two integers from `vx`, plus any integers from `ops` that were appended to `p1` because `p1[-1]` was not equal to `v2` at the time of the operation. `p2` is a list containing any integers from `ops` that were appended to `p2` because `p1[-1]` was equal to `v2` at the time of the operation. The function has printed the Hamiltonian path for each test case in the format "! v_1 v_2 ... v_n" and flushed the output buffer.
#Overall this is what the function does:The function `func` interacts with an interactor to handle multiple test cases. Each test case involves a complete undirected graph with `n` vertices and `(n - 2)` edges removed. The function queries the interactor to find a Hamiltonian path in the graph and outputs the path in the format "! v_1 v_2 ... v_n" for each test case. After processing all test cases, the function ensures that the output buffer is flushed for each query and answer. The final state of the program is that all test cases have been processed, and the Hamiltonian paths have been printed.

