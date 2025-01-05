#State of the program right berfore the function call: n and m are integers where 3 ≤ n ≤ 200,000 and 1 ≤ m ≤ 200,000; the edges are represented by pairs (u_i, v_i) where 1 ≤ u_i, v_i ≤ n and u_i ≠ v_i, with m pairs given as input.
def func_1():
    return int(raw_input())
    #The program returns an integer input obtained from the user through raw_input()
#Overall this is what the function does:The function accepts no parameters and returns an integer input obtained from the user through `raw_input()`. However, it does not handle potential input errors, such as non-integer inputs, which could raise a `ValueError`. Therefore, the function may not always return a valid integer as intended.

#State of the program right berfore the function call: n is an integer representing the number of nodes in the graph (3 ≤ n ≤ 200,000), m is an integer representing the number of edges (1 ≤ m ≤ 200,000), and each edge is represented by two distinct integers u_i and v_i (1 ≤ u_i, v_i ≤ n, u_i ≠ v_i), indicating a connection between nodes u_i and v_i.
def func_2():
    return list(map(int, raw_input().split()))
    #The program returns a list of integers obtained from user input, representing values separated by spaces
#Overall this is what the function does:The function accepts no parameters and returns a list of integers obtained from user input, where the input is a series of space-separated values read from standard input. It does not handle any input validation or exceptions, meaning that if the input is not properly formatted as integers, it could raise an error.

#State of the program right berfore the function call: n is an integer representing the number of nodes in the graph (3 ≤ n ≤ 200,000), and m is an integer representing the number of edges (1 ≤ m ≤ 200,000). Each edge is represented by a pair of integers (u_i, v_i) such that 1 ≤ u_i, v_i ≤ n and u_i ≠ v_i, indicating a connection between nodes u and v.
def func_3(n):
    stdout.write(str(n) + '\n')
#Overall this is what the function does:The function accepts an integer `n`, representing the number of nodes in a graph, and writes the value of `n` to standard output. It does not return any value.

#State of the program right berfore the function call: arr is a list of integers where the first element is the number of nodes n (3 ≤ n ≤ 200,000) and the second element is the number of edges m (1 ≤ m ≤ 200,000), followed by m pairs of integers representing the edges (u_i, v_i) such that 1 ≤ u_i, v_i ≤ n and u_i ≠ v_i.
def func_4(arr):
    pr(' '.join(map(str, arr)) + '\n')
#Overall this is what the function does:The function accepts a list of integers that represents a graph structure, where the first element indicates the number of nodes, the second element indicates the number of edges, and the subsequent pairs represent the edges between nodes. It processes this information by printing the entire list as a space-separated string followed by a newline. The function does not perform any further processing or validation of the graph structure.

#State of the program right berfore the function call: n is an integer representing the number of nodes in the graph (3 ≤ n ≤ 200,000), m is an integer representing the number of edges (1 ≤ m ≤ 200,000), and each edge is represented by a pair of distinct integers (u_i, v_i) where 1 ≤ u_i, v_i ≤ n.
def func_5():
    return map(int, stdin.read().split())
    #The program returns a list of integers parsed from the standard input, representing the edges of the graph as pairs of distinct integers (u_i, v_i) in the format of the input provided.
#Overall this is what the function does:The function accepts no parameters and returns an iterable of integers parsed from standard input. These integers represent the edges of a graph as pairs of distinct integers (u_i, v_i), but the function does not handle the case where the input format is incorrect or where there are any constraints violations; it assumes the input is well-formed according to the specified limits (3 ≤ n ≤ 200,000 and 1 ≤ m ≤ 200,000).

