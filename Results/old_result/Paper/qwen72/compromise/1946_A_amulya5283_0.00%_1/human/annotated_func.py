#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases, and test_cases is a list of tuples where each tuple contains an integer n (1 ≤ n ≤ 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func_1(t, test_cases):
    results = []
    for i in range(t):
        n, arr = test_cases[i]
        
        arr.sort()
        
        median_index = n // 2
        
        current_median = arr[median_index]
        
        heap = arr[median_index:]
        
        heapq.heapify(heap)
        
        operations = 0
        
        while heap[0] <= current_median:
            smallest = heapq.heappop(heap)
            heapq.heappush(heap, smallest + 1)
            operations += 1
        
        results.append(operations)
        
    #State: The loop has completed all its iterations, `i` is `t - 1`, `results` is a list containing the number of operations required for each test case, `n` is the first element of the last test case in `test_cases`, `arr` is the second element of the last test case in `test_cases` and is now sorted, `median_index` is `n // 2`, `current_median` is `arr[median_index]`, `heap` is a heap (min-heap) containing the elements of `arr` starting from the `median_index` to the end, but all elements in the heap are now greater than `current_median`, and `operations` is the number of times the loop executed for the last test case.
    return results
    #The program returns a list 'results' containing the number of operations required for each test case.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `test_cases`. Each tuple in `test_cases` contains an integer `n` and a list of `n` integers. The function processes each test case by sorting the list of integers, calculating the median, and then performing operations to ensure all elements in the list are greater than the median. It returns a list `results` containing the number of operations required for each test case. After the function concludes, `results` is a list of integers where each integer represents the number of operations needed for the corresponding test case. The input variables `t` and `test_cases` remain unchanged.

