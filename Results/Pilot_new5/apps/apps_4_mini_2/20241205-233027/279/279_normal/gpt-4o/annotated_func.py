#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones, with a length equal to n.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    p = list(map(int, data[1:n + 1]))
    b = list(map(int, data[n + 1:2 * n + 1]))
    visited = [False] * n
    cycles = []
    for i in range(n):
        if not visited[i]:
            cycle = []
            x = i
            while not visited[x]:
                visited[x] = True
                cycle.append(x)
                x = p[x] - 1
            cycles.append(cycle)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `p` and `b` are lists of integers with length `n`, `visited` is a list of `True` values, `cycles` contains all cycles found during the iterations, with each cycle being a list of indices that were visited in one complete traversal before returning to a previously visited index. If `n` is 0, then `cycles` is an empty list, indicating no elements to process.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `p` and `b` are lists of integers with length `n`, `visited` is a list of `True` values, `cycles` contains all cycles found during the iterations, and `no_reverse_components` is the sum of `1` for each cycle where all `b[x] == 0` for `x` in that cycle. If there is exactly one cycle in `cycles`, the value `0` has been printed. If there are multiple cycles, it outputs the value of `no_reverse_components` if it is greater than 0; otherwise, it outputs `1`.
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` representing a permutation of numbers from 1 to `n`, and a list `b` of binary values (0s and 1s) of length `n`. It identifies cycles in the permutation `p` and counts how many of these cycles consist entirely of elements in `b` that are 0. If there is exactly one cycle, it prints `0`. If there are multiple cycles, it prints the count of cycles with all zeros if it is greater than 0; otherwise, it prints `1`.

