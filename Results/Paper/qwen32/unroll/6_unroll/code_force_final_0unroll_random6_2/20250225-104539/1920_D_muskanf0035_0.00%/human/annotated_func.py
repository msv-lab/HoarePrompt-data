#State of the program right berfore the function call: n is a non-negative integer representing the number of operations, operations is a list of tuples where each tuple contains an operation type (1 or 2) and a corresponding value (x), and queries is a list of integers representing the queries.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: - `n`: Remains unchanged, as it is only used to iterate over `operations`.
    #- `operations`: Remains unchanged.
    #- `queries`: Remains unchanged.
    #- `array`: Updated based on the operations.
    #- `result`: Remains unchanged, as it is not modified within the loop.
    #
    #Given the above process, the output state is:
    #
    #Output State:
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `n`: Remains unchanged, `operations`: Remains unchanged, `queries`: Remains unchanged, `array`: Remains unchanged, `result`: `[10, 20, 10, 30]`.
    return result
    #The program returns the list [10, 20, 10, 30]
#Overall this is what the function does:The function processes a series of operations to build an array and then answers a set of queries by returning specific elements from the array based on the queries.

#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of lists where each sublist contains two integers b (1 or 2) and x (1 ≤ x ≤ n for b=1, x ≥ 1 for b=2), and queries is a list of positive integers representing the queries.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `n` is a positive integer representing the number of operations, `operations` is a list of lists where each sublist contains two integers b (1 or 2) and x (1 ≤ x ≤ n for b=1, x ≥ 1 for b=2), `queries` is a list of positive integers representing the queries, `t` is an input integer.
#Overall this is what the function does:The function `func_2` reads multiple test cases from the input. For each test case, it processes a specified number of operations and a list of queries, and then outputs the results of these queries based on the operations.

