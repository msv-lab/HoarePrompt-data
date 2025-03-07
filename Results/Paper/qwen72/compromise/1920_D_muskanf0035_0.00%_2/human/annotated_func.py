#State of the program right berfore the function call: n is a positive integer, operations is a list of tuples where each tuple contains two integers (op_type, value) such that op_type is either 1 or 2, and value is a positive integer. queries is a list of positive integers, each representing a query index.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `n` remains a positive integer, `operations` remains the same list of tuples, `queries` remains the same list of positive integers, `array` is a list containing elements based on the operations performed, and `result` remains an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: Output State: `n` remains a positive integer, `operations` remains the same list of tuples, `queries` remains the same list of positive integers, `array` is a list containing elements based on the operations performed, and `result` is a list containing the elements from `array` at the positions specified by the `queries` (where each position is adjusted by taking `(k - 1) % len(array)` for each `k` in `queries`).
    return result
    #The program returns a list `result` containing the elements from `array` at the positions specified by the `queries`, where each position is adjusted by taking `(k - 1) % len(array)` for each `k` in `queries`. The `array` is a list containing elements based on the operations performed, and `n` remains a positive integer, `operations` remains the same list of tuples, and `queries` remains the same list of positive integers.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, a list of tuples `operations` where each tuple is `(op_type, value)` with `op_type` being 1 or 2 and `value` a positive integer, and a list of positive integers `queries`. It constructs an `array` based on the operations provided: if `op_type` is 1, it appends `value` to the `array`; if `op_type` is 2, it duplicates the `array` by extending it with its current elements. The function then returns a list `result` containing the elements from `array` at the positions specified by `queries`, where each position is adjusted by taking `(k - 1) % len(array)` for each `k` in `queries`. The original `n`, `operations`, and `queries` remain unchanged.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n and q are integers such that 1 <= n, q <= 10^5, operations is a list of n lists where each inner list contains two integers b and x (b ∈ {1, 2}, 1 <= x <= n for b=1, 1 <= x <= 10^9 for b=2), and queries is a list of q integers where each integer k_i satisfies 1 <= k_i <= min(10^18, c) and c is the size of the array after all operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: The loop has executed `t` times, and for each iteration, the variables `n` and `q` have been updated with new values from the input, `operations` has been updated with a new list of `n` operations, and `queries` has been updated with a new list of `q` queries. The `result` variable has been updated with the output of `func_1(n, operations, queries)` for each iteration, and the results have been printed. The initial state of `t`, `n`, `q`, `operations`, and `queries` is reset for each iteration, so the final state of these variables is undefined after the loop completes.
#Overall this is what the function does:The function `func_2` reads multiple test cases from the standard input. For each test case, it reads the number of operations `n` and the number of queries `q`, followed by the operations and queries themselves. It then calls another function `func_1` with `n`, `operations`, and `queries` as arguments and prints the results returned by `func_1`. After processing all test cases, the function concludes, and the state of the input variables `t`, `n`, `q`, `operations`, and `queries` is undefined.

