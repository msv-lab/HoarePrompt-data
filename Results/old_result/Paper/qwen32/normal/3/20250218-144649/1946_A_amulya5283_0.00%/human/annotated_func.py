#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and test_cases is a list of tuples where each tuple contains an integer n such that 1 <= n <= 10^5, and a list of n integers a_i such that 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, test_cases is a list of tuples where each tuple contains an integer n and a list of n integers a_i, results is a list containing the value of operations for each test case, i is equal to t, n and arr are the values from the last tuple in test_cases, arr is sorted in non-decreasing order, median_index is n // 2, current_median is arr[median_index], heap is a heapified version of arr[median_index:] where the smallest element is greater than current_median, operations is the total number of operations performed in the last test case.
    return results
    #The program returns the list 'results' which contains the value of operations for each test case.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a list of integers. For each test case, it calculates the number of operations needed to ensure that all elements in the list, starting from the median, are greater than the initial median value. The function returns a list of these operation counts, one for each test case.

