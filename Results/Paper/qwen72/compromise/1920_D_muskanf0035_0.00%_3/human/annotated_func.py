#State of the program right berfore the function call: n is a positive integer, operations is a list of tuples (op_type, value) where op_type is an integer in {1, 2} and value is an integer such that 1 <= value <= n for op_type = 1 and 1 <= value <= 10^9 for op_type = 2, queries is a list of positive integers k such that 1 <= k <= min(10^18, c), where c is the size of the array after all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `n` is a positive integer, `operations` is a list of tuples (op_type, value) where op_type is an integer in {1, 2} and value is an integer such that 1 <= value <= n for op_type = 1 and 1 <= value <= 10^9 for op_type = 2, `queries` is a list of positive integers k such that 1 <= k <= min(10^18, c), where c is the size of the array after all operations, `array` is a list containing the elements appended and extended according to the operations, `result` is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `result` is a list containing the elements from `array` at the positions specified by the `queries`, where each query `k` corresponds to the element at the index `(k - 1) % len(array)`. The `array` and `queries` remain unchanged.
    return result
    #The program returns the list `result` which contains the elements from `array` at the positions specified by the `queries`, where each query `k` corresponds to the element at the index `(k - 1) % len(array)`. The `array` and `queries` remain unchanged.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (a positive integer), `operations` (a list of tuples where each tuple is `(op_type, value)` with `op_type` being an integer in {1, 2} and `value` being an integer within specific ranges based on `op_type`), and `queries` (a list of positive integers). The function processes the `operations` to build an `array` by either appending a single value (if `op_type` is 1) or duplicating the entire current `array` (if `op_type` is 2). It then returns a list `result` containing the elements from the final `array` at the positions specified by the `queries`, where each query `k` corresponds to the element at the index `(k - 1) % len(array)`. The `array` and `queries` remain unchanged after the function execution.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n and q are integers such that 1 <= n, q <= 10^5, and operations is a list of n lists where each inner list contains two integers b and x, with b in {1, 2} and 1 <= x <= 10^9 for b=2, and queries is a list of q integers k_i such that 1 <= k_i <= min(10^18, c), where c is the size of the array after all operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: The loop has finished executing all `t` iterations, and for each iteration, the `result` list has been printed. The variables `t`, `n`, `q`, `operations`, and `queries` are reset to their initial states at the beginning of each iteration, so their final values are not meaningful after the loop completes. The only lasting effect is the output produced by the `print` statement for each iteration, which consists of the results of the `func_1` function for the given `n`, `operations`, and `queries` in each iteration.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `q` from the input, followed by `n` lines of operations and `q` integers as queries. It then calls `func_1` with `n`, `operations`, and `queries` to process these inputs and prints the resulting list of integers. The function does not return any value; its primary purpose is to produce and print the results for each test case. After processing all test cases, the function completes, and the only lasting effect is the output produced by the `print` statements.

