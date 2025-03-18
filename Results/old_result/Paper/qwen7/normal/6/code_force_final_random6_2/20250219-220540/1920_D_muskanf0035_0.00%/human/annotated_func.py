#State of the program right berfore the function call: `n` is a positive integer representing the number of operations, `operations` is a list of tuples where each tuple contains two integers `(op_type, value)` indicating the type of operation and the value associated with it, and `queries` is a list of positive integers representing the positions Jayden wants to know the elements at.
def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: The `array` will contain the elements as specified by the `operations` list, and `result` will remain an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: Output State: The `queries` list has been fully iterated over, meaning `k` takes on each value in `queries` exactly once. For each iteration, `result` appends an element calculated as `array[(k - 1) % len(array)]`. Therefore, `result` is a list containing `len(queries)` elements, where each element corresponds to the value of `array[(k - 1) % len(array)]` for each `k` in `queries`.
    #
    #In simpler terms, `result` will contain `len(queries)` elements, each being the element from `array` at the index specified by `(k - 1) % len(array)` for each `k` in the original `queries` list.
    return result
    #The program returns a list `result` containing `len(queries)` elements, where each element is the element from `array` at the index specified by `(k - 1) % len(array)` for each `k` in the original `queries` list.
#Overall this is what the function does:The function accepts three parameters: `n` (a positive integer), `operations` (a list of tuples where each tuple contains two integers indicating the type of operation and the value associated with it), and `queries` (a list of positive integers representing the positions to query). After performing the specified operations on an initially empty array, it returns a list `result` containing the elements from the array at the specified indices.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, q is an integer such that 1 ≤ q ≤ 10^5, operations is a list of n lists, where each inner list contains two integers b and x such that b ∈ {1, 2}, 1 ≤ x ≤ 10^9, and queries is a list of q integers k_i such that 1 ≤ k_i ≤ min(10^18, c), where c is the size of the array after performing all operations.
def func_2():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: Output State: `t` is decremented to 0 after all iterations of the loop have finished, `n` is the final integer input for the number of operations read from the last iteration, `q` is the final integer input for the number of queries read from the last iteration, `queries` is a list of integers obtained from the last input split and converted to integers, `operations` is a list of `n` lists where each inner list contains two integers `b` and `x` such that `b ∈ {1, 2}` and `1 ≤ x ≤ 10^9`, and `result` is the return value of `func_1(n, operations, queries)` after the last iteration of the loop.
    #
    #This means that after all iterations of the loop have completed, `t` will be 0 (since it is decremented by 1 in each iteration until it reaches 0). The final values of `n` and `q` will be those provided by the last set of inputs. The `queries` list will contain the integers provided as part of the last set of inputs, and `operations` will contain the list of operations read from the last iteration. The `result` will be the output of the function `func_1` applied to the final `n`, `operations`, and `queries`.
#Overall this is what the function does:The function processes multiple sets of inputs, each consisting of the number of operations (`n`), the number of queries (`q`), a list of operations, and a list of queries. For each set, it reads the operations and queries, applies the operations to an initial array, and then answers the queries. The function ultimately prints the results of these queries for each set of inputs. After processing all sets, the function concludes with `t` (the number of sets) reduced to 0.

