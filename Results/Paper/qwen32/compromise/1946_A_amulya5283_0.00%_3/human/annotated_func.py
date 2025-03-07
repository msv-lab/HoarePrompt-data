#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. test_cases is a list of tuples, where each tuple represents a test case consisting of an integer n such that 1 <= n <= 10^5, and a list a of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is a positive integer such that 1 <= t <= 10^4, `test_cases` is a list of `t` tuples, where each tuple represents a test case consisting of an integer `n` such that 1 <= n <= 10^5, and a list `a` of `n` integers where each integer `a_i` satisfies 1 <= `a_i` <= 10^9, `results` is a list containing the value of `operations` for each of the `t` test cases, `i` is `t - 1`, `n` is the integer from the last tuple in `test_cases`, `arr` is the sorted list from the last tuple in `test_cases`, `median_index` is `n // 2`, `current_median` is `arr[median_index]`, `heap` is a heapified version of `arr[median_index:]` where all elements are greater than `current_median`, `operations` is the total number of iterations the loop executed for the last test case.`
    return results
    #The program returns `results`, which is a list containing the value of `operations` for each of the `t` test cases.
#Overall this is what the function does:The function `func_1` processes `t` test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates the number of operations needed to ensure all elements in the list are greater than the initial median of the list. The function returns a list of these operation counts for each test case.

