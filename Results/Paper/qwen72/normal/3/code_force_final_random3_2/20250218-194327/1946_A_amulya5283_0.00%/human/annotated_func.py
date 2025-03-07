#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. test_cases is a list of tuples, where each tuple contains two elements: an integer n (1 ≤ n ≤ 10^5) representing the length of the array, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the array. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `i` is `t - 1`, `results` is a list containing `t` values, each value is the number of operations required to make the smallest element in the heap greater than the current median for each test case, `n` is the first element of `test_cases[t - 1]`, `arr` is the second element of `test_cases[t - 1]` and is now sorted, `median_index` is `n // 2`, `current_median` is `arr[median_index]`, `heap` is now a min-heap containing the elements of `arr` starting from `median_index` to the end, with all elements that were less than or equal to `current_median` increased by 1 until the smallest element in the heap is greater than `current_median`, `operations` is the total number of times the smallest element in the heap was increased by 1 to make `heap[0]` greater than `current_median` for the last test case.
    return results
    #The program returns a list `results` containing `t` values, where each value represents the number of operations required to make the smallest element in the heap greater than the current median for each test case.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `test_cases`. Each tuple in `test_cases` contains an integer `n` and a list of `n` integers. The function returns a list `results` of `t` integers, where each integer represents the number of operations required to make the smallest element in the heap (formed from the second half of the sorted array) greater than the current median of the array for each test case.

