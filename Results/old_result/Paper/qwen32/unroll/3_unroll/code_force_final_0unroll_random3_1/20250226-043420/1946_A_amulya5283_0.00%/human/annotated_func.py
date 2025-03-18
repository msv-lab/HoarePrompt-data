#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each test case consists of two lines: the first line contains a single integer n such that 1 <= n <= 10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 1 <= a_i <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: results is a list containing t integers, where each integer represents the number of operations performed for the corresponding test case.
    return results
    #The program returns a list named 'results' containing t integers, where each integer represents the number of operations performed for the corresponding test case.
#Overall this is what the function does:The function `func_1` processes `t` test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates the number of operations needed to ensure that the smallest element in the list is greater than the median of the list. The function returns a list of `t` integers, where each integer represents the number of operations performed for the corresponding test case.

