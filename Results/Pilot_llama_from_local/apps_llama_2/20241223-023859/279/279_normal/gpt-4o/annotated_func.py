#State of the program right berfore the function call: There is a positive integer n, a list of integers p = [p_1, p_2,..., p_{n}] where for all i, 1 <= p_i <= n and p is a permutation, and a list of integers b = [b_1, b_2,..., b_{n}] where for all i, b_i is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer, `i` is `n-1`, `p` and `b` are lists of `n` integers, `data` is a list of strings, `visited` is a list of boolean values indicating visited nodes, and `cycles` is a list of lists representing cycles or paths within the graph.
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    if (len(cycles) == 1) :
        print(0)
    else :
        print(no_reverse_components if no_reverse_components > 0 else 1)
    #State of the program after the if-else block has been executed: *`n` is an integer, `i` is `n-1`, `p` and `b` are lists of `n` integers, `data` is a list of strings, `visited` is a list of boolean values indicating visited nodes, `cycles` is a list of lists representing cycles or paths within the graph, and `no_reverse_components` is the sum of all cycles in `cycles` where all elements in the cycle are equal to 0 in `b`. If the number of cycles is 1, then 0 has been printed. Otherwise, if `no_reverse_components` is greater than 0, then `no_reverse_components` has been printed; otherwise, 1 has been printed.
#Overall this is what the function does:The function reads input from the standard input, which consists of a positive integer n, a permutation list p of integers, and a binary list b of integers. After processing the input, it identifies cycles in the permutation p and counts the number of cycles where all elements are 0 in the binary list b. If there is only one cycle, the function prints 0. Otherwise, it prints the count of cycles with all zeros if such cycles exist; otherwise, it prints 1. The function does not return any value and only prints the result to the console. It handles the case where the number of cycles is greater than 1 and where there are cycles with and without zeros in the binary list b. The function assumes that the input is valid and does not contain any error checking or handling for invalid inputs.

