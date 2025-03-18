#State of the program right berfore the function call: The function `func()` does not take any input parameters. The input is handled through standard input as described in the problem statement: first an integer t (1 ≤ t ≤ 1000) representing the number of test cases, followed by t lines each containing a single integer n (2 ≤ n ≤ 10^5) representing the number of vertices in the graph for each test case. The sum of n over all test cases does not exceed 10^5. The function must interact with the system by outputting queries and reading responses as specified in the problem statement to determine a Hamiltonian path for each test case.
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
        
    #State: t is an integer from 1 to 1000, vx is a set containing 2 or fewer integers, ops is a list of tuples representing the operations performed for the last test case, p1 is a list containing the initial elements of vx plus any v1 values appended when p1[-1] != v2, and p2 is a list containing any v1 values appended when p1[-1] == v2. The function has processed all t test cases and output the Hamiltonian path for each.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` representing the number of vertices in a graph. For each test case, it interacts with an external system by sending queries and receiving responses to determine a Hamiltonian path in the graph. After processing all test cases, it outputs the Hamiltonian path for each graph.

