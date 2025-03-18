#State of the program right berfore the function call: n is a positive integer, operations is a list of tuples where each tuple (op_type, value) has op_type as an integer in {1, 2} and value as a positive integer, and queries is a list of positive integers such that 1 <= k <= min(10^18, c) for each k in queries, where c is the length of the array after all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `n` is a positive integer, `operations` is a list of tuples with `n` tuples, `array` is a list that contains the elements added by the operations in `operations` and possibly repeated based on the `op_type` values, `result` is an empty list, `op_type` is the last tuple's `op_type` in `operations`, and `value` is the last tuple's `value` in `operations`.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `n` is a positive integer, `operations` is a list of tuples with `n` tuples, `array` is a list that contains the elements added by the operations in `operations` and possibly repeated based on the `op_type` values, `result` is a list containing the elements at indices `(k - 1) % len(array)` for each `k` in `queries`, `op_type` is the last tuple's `op_type` in `operations`, `value` is the last tuple's `value` in `operations`, `queries` is a non-empty list.
    return result
    #The program returns the list `result` which contains the elements at indices `(k - 1) % len(array)` for each `k` in `queries`. The elements in `array` are determined by the operations specified in the `operations` list, and the final `op_type` and `value` are from the last tuple in `operations`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, a list of tuples `operations` where each tuple `(op_type, value)` specifies an operation on an array, and a list of positive integers `queries`. It constructs an array based on the operations: if `op_type` is 1, it appends `value` to the array; if `op_type` is 2, it duplicates the current array. After processing all operations, the function returns a list `result` containing the elements at indices `(k - 1) % len(array)` for each `k` in `queries`. The final state of the program includes the original `n`, the processed `operations` list, the constructed `array`, and the `result` list.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 5000, n and q are positive integers such that 1 <= n, q <= 10^5, and the sum of n and the sum of q over all test cases does not exceed 10^5.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `t` is an input integer such that 1 <= t <= 5000, `n` and `q` are specific positive integers such that 1 <= n, q <= 10^5, and the sum of n and the sum of q over all test cases does not exceed 10^5. The loop has executed `t` times, and for each execution, `operations` is a list of `n` lists containing integers from the input, `queries` is a list of integers from the input, and `result` is the value returned by `func_1(n, operations, queries)`. The variable `_` has been incremented `t` times, and `t` is now equal to the number of times the loop has executed.
#Overall this is what the function does:The function `func_2` reads a series of inputs from the user. It first reads an integer `t` (1 <= t <= 5000), which represents the number of test cases. For each test case, it reads two integers `n` and `q` (1 <= n, q <= 10^5), followed by `n` lists of integers (each representing an operation) and a list of `q` integers (representing queries). It then calls another function `func_1` with `n`, `operations`, and `queries` as arguments, and prints the result returned by `func_1`. After processing all `t` test cases, the function concludes. The final state of the program is that `t` test cases have been processed, and the results of each test case have been printed.

