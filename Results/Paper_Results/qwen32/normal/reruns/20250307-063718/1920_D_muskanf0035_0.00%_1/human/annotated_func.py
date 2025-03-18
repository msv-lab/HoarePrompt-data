#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains an integer b (either 1 or 2) and an integer x (1 <= x <= n for b=1 and x >= 1 for b=2), and queries is a list of integers representing the queries where each query is a positive integer k such that 1 <= k <= the size of the array after all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: [3, 3, 4, 3, 3, 4]
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: [3, 4, 3, 3, 4]
    return result
    #The program returns result
#Overall this is what the function does:The function `func_1` processes a series of operations to build and modify an internal array. It then answers a series of queries by returning the elements from this array based on the query indices. Each operation either appends a value to the array or duplicates the entire array. Each query specifies an index, and the function returns the element at that index in the final array, using modulo arithmetic to handle indices larger than the array size.

#State of the program right berfore the function call: n is a non-negative integer representing the number of operations, operations is a list of lists where each sublist contains two integers b (1 or 2) and x (1 ≤ x ≤ n for b=1, 1 ≤ x ≤ 10^9 for b=2), and queries is a list of q integers where each integer k_i satisfies 1 ≤ k_i ≤ min(10^18, c) with c being the size of the array after all operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: The loop has executed `t` times. For each iteration, `n` is the number of operations, `q` is the number of queries, `operations` is a list of `n` operations read from input, `queries` is a list of `q` queries read from input, and `result` is the return value of `func_1(n, operations, queries)`. The final output consists of the results from all `t` iterations, each printed on a new line.
#Overall this is what the function does:The function `func_2` reads multiple test cases from input. For each test case, it processes a series of operations on an initially empty array and then answers a set of queries about the final state of the array. The operations can either involve modifying the array or adding elements to it, and the queries ask for specific elements in the array after all operations have been performed. The results of the queries are printed for each test case.

