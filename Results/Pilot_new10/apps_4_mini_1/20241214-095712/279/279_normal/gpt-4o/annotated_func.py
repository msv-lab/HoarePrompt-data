#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of integers from 1 to n; b is a list of integers consisting of zeros and ones, where the length of b is equal to n.
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
        
    #State of the program after the  for loop has been executed: `n` is a specific positive integer such that 1 ≤ `n` ≤ 200,000; `visited` is a list of `n` boolean values indicating whether each index has been visited; `cycles` is a list containing all cycles found in the permutation represented by `p`, where each cycle is a list of indices visited in that cycle. If an index has not been visited, it indicates the presence of a cycle involving that index.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`n` is a specific positive integer such that 1 ≤ `n` ≤ 200,000, `visited` is a list of `n` boolean values indicating whether each index has been visited, `cycles` is a list representing all cycles found in the permutation `p`, and `no_reverse_components` is the sum of unvisited cycles. If there is only one cycle in `cycles`, the value `0` has been printed. If there are multiple cycles, `no_reverse_components` is printed if it is greater than 0, otherwise, `1` is printed.
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` which is a permutation of integers from 1 to `n`, and a list `b` consisting of zeros and ones with a length equal to `n`. It identifies cycles in the permutation `p` and evaluates how many of these cycles are purely composed of indices where the corresponding value in `b` is `0`. If there is only one cycle, it prints `0`. If there are multiple cycles, it prints the count of those cycles with only `0` values in `b`, unless this count is less than or equal to `0`, in which case it prints `1`.

