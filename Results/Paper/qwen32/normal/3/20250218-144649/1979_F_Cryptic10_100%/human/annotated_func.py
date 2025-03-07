#State of the program right berfore the function call: The function does not take any input variables directly. The input is provided through an interactive process where the function can make queries to learn about the graph and then output the Hamiltonian path. Specifically, for each test case, an integer n (2 ≤ n ≤ 10^5) is provided, representing the number of vertices in the graph. The function can then make up to n queries of the form "? d" (0 ≤ d ≤ n - 1) to gather information about the graph's structure. The function must output the Hamiltonian path in the format "! v1 v2 ... vn" after determining it. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop will execute for each test case provided as input. For each test case, `p1` will contain all the vertices of the graph in the order they form a Hamiltonian path, and `p2` will be empty. The final output will be the Hamiltonian path in the format "! v1 v2 ... vn".
#Overall this is what the function does:The function determines a Hamiltonian path for each test case by interactively querying the structure of a graph and outputs the path in the format "! v1 v2 ... vn". It handles multiple test cases, each with a graph containing between 2 and 100,000 vertices, and the total number of vertices across all test cases does not exceed 100,000.

