#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), p is a list of integers representing a valid permutation of length n (1 ≤ p[i] ≤ n), and b is a list of integers of length n consisting of 0s and 1s.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `visited` is a list of `n` Boolean values where all indices that were part of cycles are marked as True, `cycles` is a list of lists containing all the cycles identified in the permutation described by `p`, and `p` and `b` are lists of integers corresponding to the input values.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `visited` is a list of `n` Boolean values, `cycles` is a list of lists containing all the cycles identified in the permutation described by `p`, and `no_reverse_components` is the sum of the counts of cycles where all corresponding values in `b` are 0. If there is exactly one cycle in `cycles`, `0` has been printed. Otherwise, `no_reverse_components` remains unchanged and the output is `no_reverse_components` if it is greater than 0; otherwise, the output is 1.
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` representing a valid permutation of length `n`, and a list `b` consisting of integers (0s and 1s). It identifies cycles in the permutation defined by `p` and counts how many of these cycles consist entirely of indices where the corresponding value in `b` is `0`. If there is exactly one cycle, it prints `0`. Otherwise, it prints the count of cycles consisting entirely of 0s if the count is greater than `0`; if none of the cycles consist of 0s, it prints `1`.

