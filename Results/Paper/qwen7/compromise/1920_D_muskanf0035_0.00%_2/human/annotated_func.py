#State of the program right berfore the function call: n is a positive integer representing the number of operations, operations is a list of tuples where each tuple contains two integers (op_type, value), and queries is a list of positive integers representing the queries. op_type is either 1 or 2, where 1 indicates appending an integer to the array and 2 indicates appending the current array x times to itself. value is an integer when op_type is 1, and an integer indicating how many times to append the array when op_type is 2. The length of operations is equal to n, and the size of queries is equal to q.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: Output State: `array` is an empty list, `result` is an empty list.
    #
    #Explanation: The given loop does not modify the `result` list at all. The only operation performed on the `array` is either appending a single element or extending the array with its own elements, which results in the `array` being identical to its initial state (an empty list) after the loop completes.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: Output State: `array` is an empty list, `result` is an empty list.
    return result
    #The program returns an empty list named result
#Overall this is what the function does:The function accepts three parameters: n (a positive integer), operations (a list of tuples where each tuple contains two integers - op_type and value), and queries (a list of positive integers). Based on the op_type and value in the operations list, it either appends a single integer to an initially empty array or extends the array by repeating its contents. After processing all operations, it creates a result list by appending elements from the array based on the indices specified in the queries list, modulo the length of the array. Finally, it returns an empty list named result.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, q is an integer such that 1 ≤ q ≤ 10^5, operations is a list of n lists, each containing two integers b and x where b ∈ {1, 2}, 1 ≤ x ≤ 10^9, and queries is a list of q integers k_i such that 1 ≤ k_i ≤ min(10^18, c), where c is the size of the array after performing all n operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: After executing the loop for t times, the output state will consist of t lines, each line containing the results of calling `func_1(n, operations, queries)` for each iteration. The results are printed as a space-separated list of integers, corresponding to the answers for each query in the `queries` list for the respective iteration.
#Overall this is what the function does:The function processes a series of operations and queries over multiple iterations. For each iteration, it reads values for n and q, a list of operations, and a list of queries. It then calls another function `func_1` to handle these inputs and prints the results. The final state consists of t lines, each containing the answers to the queries for that iteration, printed as space-separated integers.

