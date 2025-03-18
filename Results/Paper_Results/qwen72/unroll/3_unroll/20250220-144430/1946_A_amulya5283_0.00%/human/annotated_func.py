#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and test_cases is a list of t test cases, where each test case is a tuple (n, a) with n being an integer such that 1 ≤ n ≤ 10^5 and a being a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, test_cases is a list of t test cases, where each test case is a tuple (n, a) with n being an integer such that 1 ≤ n ≤ 10^5 and a being a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5. results is a list of t integers, where each integer represents the number of operations required to make the smallest element in the sorted list of the corresponding test case greater than the median of that list.
    return results
    #The program returns a list 'results' containing t integers, where each integer represents the number of operations required to make the smallest element in the sorted list of the corresponding test case greater than the median of that list.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list `test_cases` of `t` tuples, each containing an integer `n` and a list `a` of `n` integers. It returns a list `results` of `t` integers, where each integer represents the number of operations required to make the smallest element in the sorted list `a` greater than the median of that list. The input `test_cases` list remains unchanged after the function execution.

