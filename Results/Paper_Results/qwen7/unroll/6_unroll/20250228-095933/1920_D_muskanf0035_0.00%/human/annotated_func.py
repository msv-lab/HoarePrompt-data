#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains two integers (op_type, value), and queries is a list of positive integers representing the indices for which we need to find the corresponding elements in the final array.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: Output State: `array` is an empty list, `result` is an empty list.
    #
    #Explanation: The given loop does not modify the `array` or `result` lists in any way that would change their state from the initial empty lists. The loop iterates over `operations`, but based on the provided code, it either appends a single value to `array` or extends `array` with its own values, which doesn't change the overall state of `array` and `result` since they are not used outside the loop conditions.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: Output State: `array` is an empty list, `result` is an empty list.
    #
    #Explanation: The loop iterates over `queries`, appending elements to `result` based on the indices specified in `queries`. However, since `array` is initially an empty list, accessing any index of `array` will result in an error (IndexError), and the loop will not execute any operations on `array` or `result`. Therefore, both `array` and `result` remain empty lists after the loop completes.
    return result
    #The program returns an empty list for result
#Overall this is what the function does:The function accepts three parameters: `n` (a positive integer), `operations` (a list of tuples where each tuple contains two integers), and `queries` (a list of positive integers). It processes the operations on an initially empty array and then returns an empty list. Regardless of the operations performed or the queries made, the function always returns an empty list.

#State of the program right berfore the function call: n is an integer representing the number of operations, q is an integer representing the number of queries, operations is a list of lists where each inner list contains two integers indicating the type of operation (1 or 2) and the value x, and queries is a list of integers representing the positions k for which the k-th element of the final array a needs to be determined.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: After all iterations, `t` times, for each query `k` in `queries`, the result is the value of the `k-th` element in the final array `a` after applying all operations from `operations` on an initial array of length `n`.
#Overall this is what the function does:The function accepts four parameters: `n` (the number of operations), `operations` (a list of operations where each operation is a list containing the type of operation and its value), and `queries` (a list of positions for which the final array values are needed). It returns a list of integers representing the values at the specified positions in the final array after performing all the operations.

