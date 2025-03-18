#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 * 10^5, p is a list of integers representing a valid permutation of the numbers 1 to n, and b is a list of integers consisting of zeros and ones with length n.
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
        
    #State of the program after the  for loop has been executed: `visited` is a list of n True values, `cycles` contains all unique cycles detected in the permutation defined by `p`, `n` remains unchanged as a positive integer.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`visited` is a list of n True values, `cycles` contains all unique cycles detected in the permutation defined by `p`, `n` remains unchanged as a positive integer, and `no_reverse_components` is the sum of boolean conditions for all cycles in `cycles`. If `len(cycles)` is equal to 1, the value 0 has been printed. Otherwise, if `no_reverse_components` is greater than 0, the printed value is `no_reverse_components`.
#Overall this is what the function does:The function processes a permutation of integers `p` from 1 to `n` and a corresponding list `b` of zeros and ones. It identifies cycles in the permutation, determining how many of these cycles consist entirely of indices with a value of 0 in `b`. If there is only one unique cycle across the entire permutation, it prints `0`. If there are multiple cycles, it prints the count of cycles that do not have any indices marked with `1` in the `b` list, unless this count is zero, in which case it prints `1`. The function does not return any value; it only prints results based on the cycle analysis. The input constraints and potential edge cases, such as handling all `1`s or mixed values in `b`, are considered, ensuring the function is robust for the specified input limits.

