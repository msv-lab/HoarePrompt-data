#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. test_cases is a list of tuples, where each tuple contains an integer n such that 1 <= n <= 10^5, and a list of n integers a_i such that 1 <= a_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: results contains the total number of operations for each test case.
    return results
    #The program returns `results`, which contains the total number of operations for each test case.
#Overall this is what the function does:The function `func_1` processes a number of test cases, each defined by a list of integers. For each test case, it calculates the number of operations needed to ensure that all elements in the list are greater than the initial median of the list. The function returns a list of these operation counts, one for each test case.

