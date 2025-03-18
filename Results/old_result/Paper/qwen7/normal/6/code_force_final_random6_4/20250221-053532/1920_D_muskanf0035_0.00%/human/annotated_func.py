#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains two integers (op_type, value), and queries is a list of positive integers representing the queries. op_type is either 1 or 2, where 1 indicates appending an integer to the end of the array, and 2 indicates appending x copies of the current array to the end. value is the integer to append when op_type is 1, and the number of copies to append when op_type is 2. The length of operations is equal to n, and the length of queries is equal to q.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: Output State: `array` is a list containing the values appended according to the operations, `result` is an empty list, and `operations` is an empty list or contains tuples that have been fully processed.
    #
    #In Natural Language: After all iterations of the loop have finished, `array` will contain all the values that were appended based on the operations provided, with each value being appended multiple times depending on the operation type (1 appends once, not 1 appends thrice). `result` remains an empty list as no operations modify it within the given loop. The `operations` list will be empty since all its tuples have been processed.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: `array` is a list containing the values appended according to the operations, `result` is a list with `len(queries)` additional elements, each being `array[(k - 1) % len(array)]` where `k` is each element of `queries` in order, and `operations` is an empty list since all its tuples have been processed.
    return result
    #The program returns a list 'result' where each element is calculated as array[(k - 1) % len(array)], with 'k' being each element from the queries list in order.
#Overall this is what the function does:The function accepts three parameters: `n` (the number of operations), `operations` (a list of tuples specifying the type of operation and the value to operate with), and `queries` (a list of positive integers representing the queries). It performs the specified operations on an initially empty array and then calculates the result for each query based on the final state of the array. The result is a list containing the queried values, where each value is determined by the formula `array[(k - 1) % len(array)]`, with `k` being each element from the `queries` list in order.

#State of the program right berfore the function call: n is an integer representing the number of operations, q is an integer representing the number of queries, operations is a list of lists where each inner list contains two integers b and x indicating the type of operation (1 or 2) and the value x, and queries is a list of integers k_i representing the positions of the elements Jayden wants to know.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: Output State: `t` must be greater than 0, `n` is an integer representing the number of operations for the last iteration, `q` is an integer representing the number of queries for the last iteration, `queries` is a list of integers representing the positions of the elements Jayden wants to know for the last iteration, `result` is the return value of `func_1(n, operations, queries)` for the last iteration.
    #
    #In this final state, after all iterations of the loop have completed, `t` will still be greater than 0 (since the loop continues as long as `t` is greater than 0), `n` and `q` will be the values corresponding to the last iteration of the loop, `queries` will be the list of integers representing the positions of the elements for the last query, and `result` will be the outcome of the `func_1` function applied to the parameters of the last iteration.
#Overall this is what the function does:The function processes a series of operations and queries. For each iteration, it reads the number of operations (`n`), the number of queries (`q`), a list of operations, and a list of query positions. It then calls `func_1` to process these inputs and returns the results of the queries. The function outputs the results for each set of operations and queries.

