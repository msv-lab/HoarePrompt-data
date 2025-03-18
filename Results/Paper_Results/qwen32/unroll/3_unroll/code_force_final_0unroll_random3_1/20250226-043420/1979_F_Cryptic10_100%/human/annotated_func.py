#State of the program right berfore the function call: The function `func()` does not take any input arguments. The interaction is handled through standard input and output as described in the problem statement. For each test case, an integer n (2 ≤ n ≤ 10^5) is provided, representing the number of vertices in the graph. The function must perform no more than n queries of the form "? d" to determine a Hamiltonian path in the graph. The interaction is non-adaptive, and the graph remains constant throughout the interaction.
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
        
    #State: the final permutation of the vertices as determined by the operations stored in `ops` and the remaining two vertices in `vx` after the while loop.
#Overall this is what the function does:The function `func` determines a Hamiltonian path in a graph with `n` vertices by performing up to `n` queries of the form "? d" through standard input and output. It does not take any input arguments and does not return a value directly; instead, it outputs the Hamiltonian path.

