#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200000; p is a list of integers representing a permutation of integers from 1 to n; b is a list of integers consisting of zeros and ones with length n.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `p` is a list of integers, `b` is a list of integers, `visited` is a list of length `n` with all values set to `True`, and `cycles` contains all the cycles found in the list `p`. Each cycle in `cycles` is a list of indices representing the indices visited in each cycle detected from the input data. If `n` is 0, then `visited` is an empty list and `cycles` remains an empty list.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer; `p` is a list of integers; `b` is a list of integers; `visited` is a list of length `n` with all values set to `True`; `cycles` contains cycles found in `p`; `no_reverse_components` is the count of cycles in `cycles` where all corresponding values in `b` are 0. If there is exactly one cycle in `cycles`, 0 has been printed. Otherwise, if the length of `cycles` is not equal to 1, the output is `no_reverse_components` if it is greater than 0; otherwise, the output is 1.
#Overall this is what the function does:The function accepts a positive integer `n`, a permutation list `p` of integers from 1 to `n`, and a list `b` of zeros and ones with length `n`. It identifies cycles in the permutation `p` and counts how many of those cycles do not have any reverse components (where all corresponding values in `b` are 0). It prints `0` if there is exactly one cycle; otherwise, it prints the count of cycles without reverse components if this count is greater than 0, or `1` if there are no such cycles.

