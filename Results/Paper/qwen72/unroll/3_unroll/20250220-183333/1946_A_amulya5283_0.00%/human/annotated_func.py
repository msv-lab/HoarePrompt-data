#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and test_cases is a list of test cases where each test case is a tuple (n, a) with n being a positive integer such that 1 <= n <= 10^5 and a being a list of n integers where 1 <= a_i <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `results` is a list of integers where each integer represents the number of operations required to make the smallest element in the sorted array of each test case greater than the median of that array. The length of `results` is equal to `t`. The variables `t` and `test_cases` remain unchanged.
    return results
    #The program returns the list `results` which contains integers representing the number of operations required to make the smallest element in the sorted array of each test case greater than the median of that array. The length of `results` is equal to `t`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of test cases `test_cases`. Each test case is a tuple `(n, a)`, where `n` is a positive integer and `a` is a list of `n` integers. It returns a list `results` of length `t`, where each element in `results` represents the number of operations required to make the smallest element in the sorted array of each test case greater than the median of that array. The input variables `t` and `test_cases` remain unchanged after the function execution.

