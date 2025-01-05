#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n, m, k ≤ 100; the input consists of n lines, each containing m integers where each integer is in the range 0 ≤ xij ≤ k, representing the instructions for each core.
def func_1():
    n, m, k = map(int, raw_input().split())
    ins = [([0] * m) for i in xrange(n + 1)]
    cell = [False] * (k + 1)
    nn = [0] * (k + 1)
    core = [0] * (n + 1)
    for i in xrange(n):
        ins[i + 1] = map(int, raw_input().split())
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `ins` is a list of `n + 1` lists where `ins[1]` to `ins[n]` contain integers from input, and `ins[0]` remains as an empty list.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `i` is `m - 1`, `k` is a non-negative integer, `j` is between `1` and `n`, `core[j]` is either `m` or a value less than `m` for each `j`, `cell[d]` is `True` for certain indices `d`, and `nn[d]` holds the last `j` index for certain valid `d`, or remains `0` if never assigned.
    for i in xrange(1, n + 1):
        print(core[i])
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `i` is `n + 1` if `n` is greater than 0, or remains `m - 1` if `n` is 0; `core[i]` for `i` from 1 to `n` has been printed.
#Overall this is what the function does:The function reads integers from input to form a list of instructions for `n` cores, where each core may be assigned a task based on the instructions. It processes `n` lines of `m` integers within the range of `0` to `k`, determining the assignment of tasks to the cores, storing the results in a list, and then prints the assignment for each core from `1` to `n`. The function does not return any value.

