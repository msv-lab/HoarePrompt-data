#State of the program right berfore the function call: n is a positive integer, operations is a list of tuples where each tuple contains two integers (op_type, value) such that op_type is 1 or 2, and value is a positive integer. If op_type is 1, then 1 <= value <= n; if op_type is 2, then 1 <= value <= 10^9. queries is a list of positive integers where each integer k satisfies 1 <= k <= min(10^18, c), and c is the size of the array after all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `n` is a positive integer, `operations` is a list of tuples with all tuples processed, `array` is a list that has been modified according to the operations in `operations`, `result` is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `n` is a positive integer, `operations` is a list of tuples with all tuples processed, `array` is a list that has been modified according to the operations in `operations`, `result` is a list containing the elements at indices `(k - 1) % len(array)` for each `k` in `queries`, `queries` must have at least as many elements as the number of iterations the loop executed.
    return result
    #The program returns a list `result` containing the elements at indices `(k - 1) % len(array)` for each `k` in `queries`. The `array` has been modified according to the operations specified in the list `operations`, and `queries` has at least as many elements as the number of iterations the loop executed.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, a list of operations where each operation is a tuple `(op_type, value)`, and a list of queries. It modifies an internal array based on the operations provided: if `op_type` is 1, it appends `value` to the array; if `op_type` is 2, it duplicates the current array. After processing all operations, it returns a list `result` where each element corresponds to the value at the index `(k - 1) % len(array)` for each query `k` in `queries`. The final state of the program includes a modified `array` and a populated `result` list, while `n` and `operations` remain unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 5000, n and q are positive integers such that 1 <= n, q <= 10^5, operations is a list of n lists where each sublist contains two integers b and x with b in {1, 2} and 1 <= x <= n for b=1 and 1 <= x <= 10^9 for b=2, queries is a list of q positive integers such that 1 <= k_i <= min(10^18, c) where c is the size of the array after all operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `t` is an input positive integer such that 1 <= `t` <= 5000 and `t` must be greater than or equal to the number of iterations the loop has executed, `n` and `q` are positive integers provided by the user input, `operations` is a list of `n` lists where each sublist contains two integers `b` and `x` with `b` in {1, 2} and 1 <= `x` <= `n` for `b`=1 and 1 <= `x` <= 10^9 for `b`=2, `queries` is a list of `q` positive integers provided by the user input, where each integer `k_i` is such that 1 <= `k_i` <= min(10^18, `c`) and `c` is the size of the array after all operations, `result` is the value returned by the function `func_1(n, operations, queries)` for each iteration, `_` is the number of iterations minus 1.
#Overall this is what the function does:The function `func_2` reads multiple sets of inputs, each set containing the number of operations `n`, the number of queries `q`, a list of operations, and a list of queries. For each set, it processes the operations and queries using the function `func_1`, and prints the results of the queries. After processing all sets, the function concludes without returning any value. The final state of the program includes the processed results being printed for each set, and the input variables `t`, `n`, `q`, `operations`, and `queries` are reset for the next set of inputs.

