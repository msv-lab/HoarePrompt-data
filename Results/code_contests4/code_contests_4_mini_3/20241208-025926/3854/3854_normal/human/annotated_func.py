#State of the program right berfore the function call: n, m, and k are positive integers such that 1 ≤ n, m, k ≤ 100, and instructions for each of the n cores consist of m integers where each integer x_ij (0 ≤ x_ij ≤ k) represents either a write command to a memory cell (1 to k) or a do-nothing command (0).
def func_1():
    n, m, k = map(int, raw_input().split())
    ins = [([0] * m) for i in xrange(n + 1)]
    cell = [False] * (k + 1)
    nn = [0] * (k + 1)
    core = [0] * (n + 1)
    for i in xrange(n):
        ins[i + 1] = map(int, raw_input().split())
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `ins` is a list containing `n` lists of integers from user input, `i` is `n - 1`.
    for i in xrange(m):
        for j in xrange(1, k + 1):
            nn[j] = 0
        
        for j in xrange(1, n + 1):
            if core[j] == 0:
                d = ins[j][i]
                if d != 0:
                    if cell[d]:
                        core[j] = i + 1
                    elif nn[d] != 0:
                        cell[d] = True
                        core[j] = core[nn[d]] = i + 1
                        nn[d] = j
                    elif nn[d] == 0:
                        nn[d] = j
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is equal to `n + m`, `k` is a positive integer, `core` contains values updated based on the conditions evaluated during the loop, `nn` may contain updated indices or remain zero for certain values, and `cell` may have some entries set to True based on the conditions processed throughout the loop.
    for i in xrange(1, n + 1):
        print(core[i])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `core` contains values updated based on the conditions evaluated during the loop, `nn` may contain updated indices or remain zero for certain values, and `cell` may have some entries set to True based on the conditions processed throughout the loop.
#Overall this is what the function does:The function accepts no parameters and processes instructions for `n` cores, each consisting of `m` integers. It tracks memory commands that could either write to a memory cell (1 to `k`) or do nothing (0). The function updates a core's state based on these commands, printing the final state of each core after processing all instructions. The logic ensures that it handles cases where memory cells are already written to, as well as tracking the most recent core that accessed a specific memory cell. It does not handle invalid inputs or edge cases where `n`, `m`, or `k` are out of the specified bounds.

