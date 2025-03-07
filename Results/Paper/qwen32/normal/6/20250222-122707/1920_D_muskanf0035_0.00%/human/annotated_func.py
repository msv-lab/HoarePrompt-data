#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains an integer b (either 1 or 2) and an integer x (1 ≤ x ≤ n if b=1, 1 ≤ x ≤ 10^9 if b=2), and queries is a list of integers where each integer k satisfies 1 ≤ k ≤ min(10^18, c) with c being the size of the array after all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: the final list `array` after all operations have been processed.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: - `result` will contain as many elements as there are in `queries`.
    #- Each element in `result` corresponds to an element in `array` selected by the index `(k - 1) % len(array)` where `k` is each element from `queries`.
    #
    #In simple terms, after all iterations, `result` will be a list of elements from `array` selected according to the indices specified by `queries`, with the indices adjusted to wrap around `array` if necessary.
    #
    #Output State:
    return result
    #The program returns `result`, which is a list of elements from `array` selected according to the indices specified by `queries`, with the indices adjusted to wrap around `array` if necessary.
#Overall this is what the function does:The function processes a series of operations to build an array and then selects elements from this array based on a list of queries. Each query specifies an index, and the function retrieves the corresponding element from the array, adjusting the index to wrap around if it exceeds the array's length. The function returns a list of these selected elements.

#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of lists where each sublist contains two integers b (1 or 2) and x (1 ≤ x ≤ n for b=1, x ≥ 1 for b=2), and queries is a list of q positive integers representing the queries.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `t` is 0, `n`, `q`, `operations`, `queries`, and `result` are the values from the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of operations and queries. For each test case, it processes a series of operations and then answers a series of queries, outputting the results for each query.

