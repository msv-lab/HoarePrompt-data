#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and test_cases is a list of tuples. Each tuple contains an integer n (the length of the array a) followed by n integers representing the array a. Additionally, the sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `results` is a list containing the total number of operations performed across all test cases, `i` is equal to the total number of test cases, `operations` is the sum of operations performed for each test case, and `heap` is empty.
    #
    #Explanation: After all iterations of the loop, `results` will contain the total number of operations performed across all test cases. The value of `i` will be equal to the total number of test cases since the loop runs for each test case exactly once. The variable `operations` will hold the sum of operations performed for each test case. Since the loop processes each test case and empties the heap at the end, the heap will be empty.
    return results
    #`results` is a list containing the total number of operations performed across all test cases, `i` is equal to the total number of test cases, `operations` is the sum of operations performed for each test case, and `heap` is empty.
#Overall this is what the function does:The function accepts two parameters: `t`, a positive integer representing the number of test cases, and `test_cases`, a list of tuples where each tuple contains an integer `n` (the length of the array `a`) followed by `n` integers representing the array `a`. It calculates the number of operations required to ensure that the smallest element in the second half of each array is greater than the median of the array. For each test case, it sorts the array, finds the median, and uses a min-heap to increment elements until the smallest element in the second half is greater than the median. It then sums up the operations for all test cases and returns a list containing these totals, the total number of test cases, and an empty heap.

