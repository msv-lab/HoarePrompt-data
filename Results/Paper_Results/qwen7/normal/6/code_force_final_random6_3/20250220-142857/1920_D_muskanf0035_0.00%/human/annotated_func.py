#State of the program right berfore the function call: operations is a list of tuples, where each tuple contains two integers (op_type, value). op_type is either 1 or 2, indicating the type of operation. If op_type is 1, value is an integer x (1 ≤ x ≤ n) representing the integer to append to the array. If op_type is 2, value is an integer x (1 ≤ x ≤ 10^9) representing the number of copies to append to the array. queries is a list of integers k_i (1 ≤ k_i ≤ min(10^18, c)), where c is the size of the array after performing all operations.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: Output State: `array` is a list where elements are either appended based on the operation type or repeated twice depending on previous operations, `result` is an empty list, and `operations` is an empty list after all iterations.
    #
    #In more detail, after the loop has executed all its iterations:
    #- The `array` will contain elements that were appended when `op_type` was 1, or those elements will be repeated twice if they were previously extended (based on the second part of the loop body).
    #- The `result` remains an empty list as no values are added to it within the loop.
    #- The `operations` list becomes empty since all operations have been processed.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: The `result` list will contain all elements from `array` that correspond to the indices specified by `queries`. The `array` and `operations` lists will be empty since no new elements are appended to `array` and all operations are processed.
    return result
    #The program returns an empty list 'result' since no elements are added to it and all operations are processed.
#Overall this is what the function does:The function processes a list of operations to modify an array and then generates a result list based on given queries. Specifically, it appends integers to or repeats elements in the array according to the operation type. After processing all operations, it creates a result list by indexing into the modified array using the provided queries, and finally returns an empty list since no elements are added to the result list during the process.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, q is an integer such that 1 ≤ q ≤ 10^5, operations is a list of n lists, each containing two integers b and x where b ∈ {1, 2}, 1 ≤ x ≤ 10^9, and queries is a list of q integers k_i where 1 ≤ k_i ≤ min(10^18, c), and c is the size of the array after performing all n operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: After the loop executes all the iterations, `t` will be 0, `queries` will be a list of integers from the final input, `n` will be the first integer from the final input, `q` will be the second integer from the final input, `operations` will be updated to a list of `n` lists, each containing two integers \(b\) and \(x\) where \(b \in \{1, 2\}\) and \(1 \leq x \leq 10^9\), and `result` will be the return value of `func_1(n, operations, queries)`
#Overall this is what the function does:The function `func_2` accepts an integer `t`, followed by `t` sets of inputs. Each set includes integers `n` and `q`, a list of `n` operations, and a list of `q` queries. It processes `n` operations on an array and then answers `q` queries based on the final state of the array after all operations are applied. The function prints the results of the queries for each set of inputs.

