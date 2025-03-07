#State of the program right berfore the function call: The function operates in an interactive environment where the input is provided through a series of queries and responses. The input consists of multiple test cases, each with an integer n (2 ≤ n ≤ 10^5) representing the number of vertices in a graph. The graph is initially a complete undirected graph with n vertices, from which (n - 2) edges have been removed. The function can make at most n queries of the form "? d" (0 ≤ d ≤ n - 1) to the interactor, and must output a Hamiltonian path for each test case. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop has completed all iterations, and the final state is as follows: `vx` is a set containing exactly 2 integers from the original set of integers from 1 to `int(input())`. `ops` is a list containing all tuples generated during the loop execution, where each tuple represents an operation. `p1` is a list containing the 2 integers from `vx` plus all `v1` values from `ops` where the corresponding `v2` did not match the last element of `p1` at the time of the operation. `p2` is a list containing all `v1` values from `ops` where the corresponding `v2` matched the last element of `p1` at the time of the operation. The final output is a string "! " followed by the elements of `p1` in reverse order and then the elements of `p2` in the order they were appended.
#Overall this is what the function does:The function operates in an interactive environment and does not accept any explicit parameters. It handles multiple test cases, each defined by an integer n (2 ≤ n ≤ 10^5) representing the number of vertices in a complete undirected graph from which (n - 2) edges have been removed. The function can make at most n queries to the interactor to determine the structure of the graph. For each test case, the function outputs a Hamiltonian path, which is a sequence of vertices that visits each vertex exactly once. The final state of the program after the function concludes is that all test cases have been processed, and a Hamiltonian path has been output for each test case.

