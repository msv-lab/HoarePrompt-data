#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and test_cases is a list of tuples. Each tuple contains an integer n (the length of the array a) followed by n integers representing the array a. The length of each array a satisfies 1 <= n <= 10^5 and each element of the array a satisfies 1 <= a_i <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: `operations` is 3 for each iteration, `t` is the total number of test cases, `i` ranges from 0 to `t-1`, `n` is the first element of `test_cases[i]` for each iteration, `arr` is a sorted version of the second element of `test_cases[i]` for each iteration, `median_index` is `n // 2`, `current_median` remains unchanged as it is the value of `arr[median_index]` for each iteration, `heap` is a heap data structure starting from `arr[median_index]` to the end of `arr` for each iteration, `heap[0]` is the original smallest element plus 3 for each iteration, `smallest` holds the original smallest element for each iteration, `heap` has been updated to include `smallest + 1` three times for each iteration, and `results` is a list containing 3 for each iteration.
    #
    #This means that for every test case, the loop performs exactly 3 operations, and the `results` list will contain 3 for each test case after all iterations of the loop have completed.
    return results
    #The program returns a list of 3 for each test case after all iterations of the loop have completed.
#Overall this is what the function does:The function accepts two parameters: `t` (a positive integer representing the number of test cases) and `test_cases` (a list of tuples). Each tuple contains an integer `n` (the length of the array `a`) followed by `n` integers representing the array `a`. For each test case, the function sorts the array, finds the median, creates a heap from the elements greater than or equal to the median, and performs a series of operations where it increments the smallest element in the heap until it exceeds the median. After processing all test cases, the function returns a list where each element is 3, indicating that exactly 3 operations were performed for each test case.

