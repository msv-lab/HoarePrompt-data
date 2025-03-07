#State of the program right berfore the function call: n is a non-negative integer representing the number of operations, operations is a list of tuples where each tuple contains an integer op_type (either 1 or 2) and an integer value, and queries is a list of integers representing the positions to query in the array.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `array` is the final list after all operations have been applied, `n` remains the same, `operations` is empty, `queries` remains the same, and `result` remains an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `array` is the final list after all operations have been applied, `n` remains the same, `operations` is empty, `queries` is empty, and `result` is a list containing elements `array[(k - 1) % len(array)]` for each `k` in the original `queries` list.
    return result
    #The program returns `result`, which is a list containing elements `array[(k - 1) % len(array)]` for each `k` in the original `queries` list.
#Overall this is what the function does:The function accepts three parameters: `n`, a non-negative integer representing the number of operations; `operations`, a list of tuples where each tuple contains an integer `op_type` (either 1 or 2) and an integer `value`; and `queries`, a list of integers representing the positions to query in the array. The function performs a series of operations on an array based on the `operations` list and then returns a list of elements from the array based on the positions specified in `queries`. Each element in the result list corresponds to the element at the position `(k - 1) % len(array)` for each `k` in the `queries` list.

#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of lists where each sublist contains two integers (b, x) with b being either 1 or 2 and x being a positive integer, and queries is a list of positive integers representing the queries.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `t` is 0, `n`, `q`, `operations`, `queries`, and `result` are the values from the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of operations and queries. For each test case, it processes a series of operations and then answers a set of queries based on the results of those operations. The function outputs the answers to the queries for each test case.

