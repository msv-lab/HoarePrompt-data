#State of the program right berfore the function call: n is a positive integer, operations is a list of tuples where each tuple contains two integers (op_type, value) such that op_type is either 1 or 2, and value is a positive integer. queries is a list of positive integers, each representing a query index k, where 1 <= k <= min(10^18, c) and c is the size of the array after all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `n` is a positive integer, `operations` is a list of tuples where each tuple contains two integers (op_type, value) such that op_type is either 1 or 2, and value is a positive integer. `queries` is a list of positive integers, each representing a query index k, where 1 <= k <= min(10^18, c) and c is the size of the array after all operations. `array` is a list that has been modified according to the operations specified in the `operations` list. If an operation is of type 1, the value is appended to the `array`. If an operation is of type 2, the `array` is extended by duplicating its current elements. `result` is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `n` is a positive integer, `operations` is a list of tuples, `queries` is a non-empty list of positive integers, `array` is a list modified according to the operations, `result` is a list containing the elements at indices `(k - 1) % len(array)` of `array` for each `k` in `queries`.
    return result
    #The program returns a list `result` containing the elements at indices `(k - 1) % len(array)` of `array` for each `k` in `queries`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, a list of tuples `operations` where each tuple contains an operation type (1 or 2) and a positive integer value, and a list of positive integers `queries`. It modifies an array based on the operations specified in `operations`: appending the value if the operation type is 1, or duplicating the current elements of the array if the operation type is 2. After processing all operations, the function returns a list `result` containing the elements at the indices `(k - 1) % len(array)` of the modified array for each query index `k` in `queries`. The final state of the program includes the modified `array` and the `result` list, which contains the queried elements.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 5000, n and q are positive integers such that 1 <= n, q <= 10^5, operations is a list of n lists where each inner list contains two integers b and x, and queries is a list of q positive integers.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `t` is an input integer such that 1 <= t <= 5000, `n` and `q` are positive integers provided by the user such that 1 <= n, q <= 10^5, `operations` is a list of `n` lists where each inner list contains two integers provided by the user, `queries` is a list of `q` positive integers provided by the user, `result` is the value returned by `func_1(n, operations, queries)`, `_` is incremented by 1 for each iteration and must be less than `t` for the loop to continue, the loop has executed `t` times, and all results have been printed.
#Overall this is what the function does:The function `func_2` processes `t` test cases, where `t` is a positive integer such that 1 <= t <= 5000. For each test case, it reads two positive integers `n` and `q` (1 <= n, q <= 10^5), a list of `n` operations where each operation is a list of two integers `[b, x]`, and a list of `q` positive integers `queries`. It then calls `func_1` with `n`, `operations`, and `queries` as arguments and prints the resulting list of values. After processing all `t` test cases, the function has printed the results for each test case, and the program state is such that all inputs have been consumed and all results have been printed.

