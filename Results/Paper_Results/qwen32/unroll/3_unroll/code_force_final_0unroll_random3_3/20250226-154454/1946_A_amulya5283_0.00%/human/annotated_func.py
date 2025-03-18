#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), test_cases is a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 10^5) and a list of n integers a_i (1 ≤ a_i ≤ 10^9) representing the array a. The sum of all n across all test cases does not exceed 2 × 10^5.
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
        
    #State: `results` is a list containing the number of operations for each test case, and `t`, `test_cases` remain unchanged.
    return results
    #The program returns the list `results` which contains the number of operations for each test case.
#Overall this is what the function does:The function `func_1` takes a positive integer `t` representing the number of test cases and a list of tuples `test_cases`. Each tuple contains an integer `n` and a list of `n` integers. The function processes each test case to determine the number of operations needed to ensure that the smallest element in the second half of the sorted array is greater than the median. It returns a list of these operation counts corresponding to each test case.

