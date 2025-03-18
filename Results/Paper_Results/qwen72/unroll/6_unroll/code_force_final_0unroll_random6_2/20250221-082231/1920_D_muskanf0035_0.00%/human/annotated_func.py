#State of the program right berfore the function call: n is a positive integer, operations is a list of tuples where each tuple contains two integers (op_type, value) such that op_type is either 1 or 2, and value is a positive integer. If op_type is 1, then 1 <= value <= n. If op_type is 2, then 1 <= value <= 10^9. queries is a list of positive integers where each integer k satisfies 1 <= k <= min(10^18, c), and c is the size of the array after all n operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `array` contains the elements appended and extended based on the operations list, and `result` remains an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `array` remains unchanged, and `result` contains the elements from `array` at the indices `(k - 1) % len(array)` for each `k` in `queries`.
    return result
    #The program returns a list `result` containing the elements from `array` at the indices `(k - 1) % len(array)` for each `k` in `queries`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, a list of tuples `operations` where each tuple represents an operation type and a value, and a list of positive integers `queries`. It modifies an internal array based on the operations provided: if the operation type is 1, it appends the value to the array; if the operation type is 2, it duplicates the array by extending it with its current elements. After processing all operations, the function returns a list `result` containing the elements from the array at the indices `(k - 1) % len(array)` for each `k` in `queries`. The final state of the program includes the modified array and the returned `result` list.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 5000. n and q are positive integers such that 1 <= n, q <= 10^5. operations is a list of n lists, each containing two integers b and x, where b is either 1 or 2, and x is an integer such that 1 <= x <= n if b=1, and 1 <= x <= 10^9 if b=2. queries is a list of q integers, each representing a query index k_i such that 1 <= k_i <= min(10^18, c), where c is the size of the array after all operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: After all iterations of the loop, `t` is an input integer such that 1 <= t <= 5000, `n` and `q` are positive integers such that 1 <= n, q <= 10^5, `operations` is a list of n lists, each containing two integers b and x, where b is either 1 or 2, and x is an integer such that 1 <= x <= n if b=1, and 1 <= x <= 10^9 if b=2, `queries` is a list of q integers, each representing a query index k_i such that 1 <= k_i <= min(10^18, c), where c is the size of the array after all operations. The loop will have printed the results of `func_1(n, operations, queries)` for each test case, and the variables `n`, `q`, `operations`, and `queries` will be reinitialized for each test case.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `q` from the input, followed by `n` lines of operations and `q` integers representing queries. It then calls another function `func_1` with `n`, `operations`, and `queries` as arguments, and prints the results returned by `func_1`. After processing all test cases, the function has printed the results for each test case, and the variables `n`, `q`, `operations`, and `queries` are reinitialized for each test case. The function does not return any value.

