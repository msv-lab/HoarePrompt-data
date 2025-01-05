#State of the program right berfore the function call: n and m are integers such that 3 <= n <= 200,000 and 1 <= m <= 200,000. The input graph is simple (no self-loops, at most one edge between every pair of nodes).**
def func_1():
    return int(raw_input())
    #The program returns the integer value obtained from the raw input
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads the raw input and returns the integer value obtained from it.

#State of the program right berfore the function call: n and m are positive integers such that 3 <= n <= 200,000 and 1 <= m <= 200,000. Each pair of integers u_i and v_i (1 ≤ u_i, v_i ≤ n, u_i ≠ v_i) represents an edge between nodes u and v in the graph.**
def func_2():
    return list(map(int, raw_input().split()))
    #The program returns a list of integers obtained by mapping the input values after splitting them
#Overall this is what the function does:The function func_2 does not accept any parameters. It reads input values, splits them, maps them to integers, and returns a list of those integers. The function lacks validation for input format, potential errors during input reading, or handling of invalid input values.

#State of the program right berfore the function call: **Precondition**: **n is an integer such that 3 <= n <= 200,000.**
def func_3(n):
    stdout.write(str(n) + '\n')
#Overall this is what the function does:The function `func_3` accepts an integer parameter `n` with the constraint 3 <= n <= 200,000 and prints the value of `n` followed by a newline character. The function does not have a specific output or return value as described in the given constraints.

#State of the program right berfore the function call: n and m are positive integers such that 3 ≤ n ≤ 200,000 and 1 ≤ m ≤ 200,000. arr is a list of tuples representing the edges in the graph. Each tuple contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v).**
def func_4(arr):
    pr(' '.join(map(str, arr)) + '\n')
#Overall this is what the function does:The function `func_4` accepts a parameter `arr`, which is a list of tuples representing the edges in a graph. Each tuple contains two integers u and v. The function then prints the elements of each tuple in the list `arr` separated by a space. The parameter constraints dictate that `n` and `m` are positive integers such that 3 ≤ n ≤ 200,000 and 1 ≤ m ≤ 200,000. The function does not explicitly return a value, but it outputs the elements of the tuples in `arr` formatted as a string.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= 200,000 and 1 <= m <= 200,000. Each pair of integers u_i and v_i (1 ≤ u_i, v_i ≤ n, u_i ≠ v_i) represents an edge between nodes u and v in the graph.**
def func_5():
    return map(int, stdin.read().split())
    #The program returns a map object containing integers after reading input from stdin
#Overall this is what the function does:The function `func_5` reads input from stdin to obtain integers `n` and `m`, where `n` and `m` are integers satisfying the constraints 3 <= n <= 200,000 and 1 <= m <= 200,000. Each pair of integers u_i and v_i (1 ≤ u_i, v_i ≤ n, u_i ≠ v_i) represents an edge between nodes u and v in the graph. The function then returns a map object containing integers.

