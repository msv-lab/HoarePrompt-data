#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains an integer b (either 1 or 2) and an integer x (1 ≤ x ≤ n for b=1 and 1 ≤ x ≤ 10^9 for b=2), and queries is a list of positive integers representing the queries.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: n is 5, operations is [(1, 3), (2, 0), (1, 5), (2, 0)], queries is [1, 2, 3], array is [3, 3, 5, 3, 3, 5], result is [].
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: n is 5, operations is [(1, 3), (2, 0), (1, 5), (2, 0)], queries is [1, 2, 3], array is [3, 3, 5, 3, 3, 5], result is [3, 3, 5].
    return result
    #The program returns result which is [3, 3, 5]
#Overall this is what the function does:The function `func_1` processes a series of operations to build an array and then uses a list of queries to retrieve specific elements from this array, returning the results of these queries.

#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of lists where each sublist contains two integers b and x, with b being either 1 or 2, and x being a positive integer, and queries is a list of positive integers representing the queries.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: `n` is the number of operations for the last iteration, `q` is the number of queries for the last iteration, `operations` is the list of operations for the last iteration, `queries` is the list of queries for the last iteration, and `result` is the output of `func_1` for the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of operations and queries. For each test case, it processes a list of operations and a list of queries, and then outputs the results of the queries based on the operations.

