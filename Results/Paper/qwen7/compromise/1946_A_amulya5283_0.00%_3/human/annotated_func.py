#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and test_cases is a list of tuples. Each tuple contains an integer n (the length of the array a) followed by n integers a_1, a_2, \ldots, a_n (each a_i is an integer between 1 and 10^9 inclusive). The length of each array a is between 1 and 10^5, and the sum of all lengths n across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: `results` is a list containing the total number of operations performed for all test cases, `t` is a positive integer, `test_cases` is a list of tuples, `i` is equal to `t-1`, `n` is the last element's first value from `test_cases`, `arr` is the sorted second element of the last tuple in `test_cases`, `median_index` is `n // 2`, `current_median` is `arr[median_index] - 3 * t`, `heap` is a heap data structure starting from `arr[median_index + 3 * t]` to the end of `arr` with each element incremented by 6 * t, `operations` is the total number of operations performed across all test cases, and `smallest` is the smallest element popped from `heap`, with `smallest + 1` being pushed onto `heap`.
    return results
    #The program returns a list named 'results' which contains the total number of operations performed for all test cases.
#Overall this is what the function does:The function accepts two parameters: `t`, a positive integer representing the number of test cases, and `test_cases`, a list of tuples where each tuple contains an integer `n` (the length of the array `a`) followed by `n` integers `a_1, a_2, ..., a_n` (each `a_i` is an integer between 1 and 10^9 inclusive). For each test case, it sorts the array, finds the median, and then performs operations on a subset of the array using a heap data structure. It counts the number of operations needed to ensure all elements in the heap are greater than the median. Finally, it returns a list named 'results' containing the total number of operations performed for all test cases.

