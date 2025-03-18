#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases, and test_cases is a list of t tuples, where each tuple contains two elements: an integer n (1 ≤ n ≤ 10^5) representing the length of the array, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the array a. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `test_cases` is a list of t tuples, `results` is a list containing the number of operations required for each of the t test cases to ensure all elements in the heap are greater than the current median, `i` is `t - 1`, `n` is the first element of the last tuple in `test_cases`, `arr` is the sorted version of the second element of the last tuple in `test_cases`, `median_index` is `n // 2`, `current_median` is the value at the index `median_index` in `arr`, `heap` is a min-heap containing elements from `arr` starting from index `median_index` to the end, where all elements are strictly greater than `current_median`, and `operations` is the number of times the loop executed for the last test case.
    return results
    #The program returns the list 'results' containing the number of operations required for each of the t test cases to ensure all elements in the heap are greater than the current median.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of `t` tuples, each containing an integer `n` and a list of `n` integers. It returns a list `results` where each element represents the number of operations required to ensure all elements in the corresponding heap (constructed from the sorted array starting from the median) are greater than the current median. The function modifies the input arrays by sorting them but does not alter the original `test_cases` list. After the function concludes, `t` remains a positive integer, `test_cases` is unchanged, and `results` contains the operation counts for each test case.

