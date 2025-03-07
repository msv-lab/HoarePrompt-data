#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and test_cases is a list of tuples where each tuple contains an integer n (1 <= n <= 10^5) and a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: results is a list of integers where each integer represents the number of operations required for the corresponding test case to ensure that the smallest element in the heap is greater than the current median.
    return results
    #The program returns a list of integers where each integer represents the number of operations required for the corresponding test case to ensure that the smallest element in the heap is greater than the current median.
#Overall this is what the function does:The function `func_1` processes a set of test cases, each consisting of a list of integers. For each test case, it calculates the number of operations needed to ensure that the smallest element in a heap (constructed from the second half of the sorted list) is greater than the median of the original list. The function returns a list of these operation counts corresponding to each test case.

