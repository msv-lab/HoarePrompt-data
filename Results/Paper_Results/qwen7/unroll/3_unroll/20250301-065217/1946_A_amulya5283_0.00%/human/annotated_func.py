#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and test_cases is a list of tuples. Each tuple contains an integer n (the length of the array a) and a list of n integers a_1, a_2, \ldots, a_n (the array a).
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
        
    #State: Output State: `t` is a positive integer representing the number of test cases, `test_cases` is a list of tuples, each containing an integer `n` and a list of `n` integers `a`, `results` is a list of integers where each integer represents the number of operations performed for each test case.
    return results
    #The program returns a list of integers called 'results', where each integer represents the number of operations performed for each test case.
#Overall this is what the function does:The function processes a list of test cases, where each test case consists of an integer `n` and an array of `n` integers. For each test case, it calculates the number of operations required to ensure that the smallest element in a min-heap (initialized with the second half of the sorted array) is greater than the median value of the original array. The function returns a list of integers, where each integer represents the number of operations performed for each test case.

