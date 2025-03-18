#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^5, p is a list of n integers representing a permutation, and b is a list of n integers consisting only of 0s and 1s.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `p` is a list of integers, `b` is a list of integers, `data` is a list of strings, `visited` is a list of boolean values where each element indicates if the corresponding index was visited during the loop, `cycles` is a list of lists representing the cycles found in the graph defined by `p`.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `p` is a list of integers, `b` is a list of integers, `data` is a list of strings, `visited` is a list of boolean values indicating if the corresponding index was visited during the loop, `cycles` is a list of lists representing the cycles found in the graph defined by `p`, and `no_reverse_components` is the sum of boolean values determined by whether all elements in each cycle are equal to 0 in the list `b`. If the length of `cycles` is exactly 1, a value of `0` is printed. Otherwise, if `no_reverse_components` is greater than 0, it is printed; otherwise, `1` is printed.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `p`, and `b`. Here, `n` is an integer such that \(1 \leq n \leq 2 \cdot 10^5\), `p` is a list of `n` integers representing a permutation, and `b` is a list of `n` integers consisting only of 0s and 1s. The function identifies cycles in the permutation `p` and checks if all elements within each cycle in `b` are 0s. If there is only one cycle, it prints `0`. Otherwise, it prints the number of cycles where all elements in `b` are 0s, unless no such cycles exist, in which case it prints `1`. The function handles the following edge cases:
- If `n` is 1, there is only one cycle, and it always prints `0`.
- If all elements in `b` are 0s across all cycles, the function prints the count of cycles where all elements are 0s.
- If no cycles have all elements in `b` being 0s, the function prints `1`.
The function does not modify the input lists `p` and `b`, and it returns nothing (i.e., it prints the result directly).

