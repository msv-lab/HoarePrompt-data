#State of the program right berfore the function call: n and m are integers such that 3 <= n <= 200000 and 1 <= m <= 200000. u_i and v_i are integers such that 1 <= u_i, v_i <= n and u_i != v_i.**
def func_1():
    return int(raw_input())
    #The program returns an integer obtained from user input
#Overall this is what the function does:The function `func_1` does not accept any parameters. It prompts the user for an integer input and returns the input value as an integer. The function does not have any error handling for non-integer inputs or invalid inputs.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= 200,000 and 1 <= m <= 200,000. Each pair (u_i, v_i) in the input represents an edge between nodes u and v in the graph.**
def func_2():
    return list(map(int, raw_input().split()))
    #The program returns a list of integers after mapping the input values that are split by spaces
#Overall this is what the function does:The function `func_2` does not accept any parameters. It processes input values by splitting them with spaces and returns a list of integers after mapping them. The function lacks handling of any errors or edge cases related to the input values.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 200,000.**
def func_3(n):
    stdout.write(str(n) + '\n')
#Overall this is what the function does:The function `func_3` accepts an integer `n` within the range 3 <= n <= 200,000 and prints the value of `n` followed by a newline character. The function does not return any specific value.

#State of the program right berfore the function call: arr is a list of tuples where each tuple contains two integers representing an edge between two nodes in the graph.**
def func_4(arr):
    pr(' '.join(map(str, arr)) + '\n')
#Overall this is what the function does:The function `func_4` accepts a parameter `arr`, which is a list of tuples where each tuple represents an edge between two nodes in a graph. The function then prints the elements of the tuples in `arr` separated by spaces followed by a newline character. The function does not have a return value.

#State of the program right berfore the function call: n and m are integers such that 3 ≤ n ≤ 200,000 and 1 ≤ m ≤ 200,000. The input graph is a simple graph without self-loops.**
def func_5():
    return map(int, stdin.read().split())
    #The program returns a map object of integers created by converting the input read from standard input
#Overall this is what the function does:The function `func_5` reads input from standard input and returns a map object of integers created by converting the input. The function does not accept any parameters. It converts the input read from standard input into a map object containing integers.

