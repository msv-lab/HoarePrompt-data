#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains an integer b (either 1 or 2) and an integer x (1 <= x <= n for b=1, x >= 1 for b=2), and queries is a list of integers where each integer k satisfies 1 <= k <= len(array) after all operations are performed.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: n is a positive integer, operations is a list of tuples, queries is a list of integers, array is the final modified list after all operations, result is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: - After the loop finishes, `result` will contain elements from `array` at positions determined by the indices calculated from `queries`.
    #   - The state of `n`, `operations`, `queries`, and `array` remains unchanged as they are not modified within the loop.
    #
    #Given this understanding, the output state can be described as follows:
    #
    #Output State:
    return result
    #The program returns `result` which contains elements from `array` at positions determined by the indices calculated from `queries`.
#Overall this is what the function does:The function takes a positive integer `n`, a list of operations, and a list of queries. It modifies an initially empty array based on the operations and returns a list of elements from the array at positions specified by the queries. Each operation either appends a value to the array or duplicates the array. The queries are indices into the final array, and the function handles indices larger than the array length by using modulo arithmetic.

#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of lists where each sublist contains two integers b and x describing the type and value of each operation, and queries is a list of positive integers representing the queries.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: The variables `n`, `operations`, `queries`, and `t` will retain their values from the last iteration of the loop, but the actual output will be a series of results printed to the console for each iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of operations and queries. For each test case, it processes the operations and outputs the results corresponding to the queries.

