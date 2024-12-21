#State of the program right berfore the function call: n is a positive integer, p is a permutation of integers from 1 to n, and b is a sequence of zeros and ones of length n.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `p` is a list of integers from the original `data[1]` to the original `data[n]`, `b` is a list of `n` zeros and ones, `data` is a consumed list of strings, `visited` is a list of `n` boolean values where all indices that were part of a detected cycle are `True`, and `cycles` is a list of detected cycles, where each cycle is a list of indices that form a cycle.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: `n` is a non-negative integer, `p` is a list of integers from the original `data[1]` to the original `data[n]`, `b` is a list of `n` zeros and ones, `data` is a consumed list of strings, `visited` is a list of `n` boolean values where all indices that were part of a detected cycle are `True`, `cycles` is a list of detected cycles, where each cycle is a list of indices that form a cycle. If `len(cycles)` is 1, the value 0 has been printed. Otherwise, `no_reverse_components` is either its current value if greater than 0 or 1, which has been returned.
#Overall this is what the function does:The function reads input from the standard input, parses it into three variables: `n`, a positive integer, `p`, a permutation of integers from 1 to `n`, and `b`, a sequence of zeros and ones of length `n`. It then detects cycles in the permutation `p` and counts the number of cycles where all elements have a corresponding value of 0 in `b`. If there is only one cycle, it prints 0; otherwise, it prints the count of cycles without any 1s in their corresponding `b` values if such cycles exist, or 1 if no such cycles exist. The function modifies the state of the program by consuming the input, calculating and storing intermediate values, and printing the result, but it does not modify the input data itself. It handles cases where the input permutation may contain any number of cycles, including the edge case where there is only one cycle. The function does not perform any error handling on the input data, so it assumes that the input will always be in the correct format.

