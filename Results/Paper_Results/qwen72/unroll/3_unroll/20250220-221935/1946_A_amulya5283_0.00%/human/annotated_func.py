#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases. test_cases is a list of tuples, where each tuple contains two elements: an integer n (1 ≤ n ≤ 10^5) representing the length of the array, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the array a. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases. `test_cases` is a list of tuples, where each tuple contains two elements: an integer n (1 ≤ n ≤ 10^5) representing the length of the array, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the array a. The sum of the values of n over all test cases does not exceed 2 · 10^5. `results` is a list of integers, where each integer represents the number of operations required to make all elements in the corresponding array greater than the initial median of that array.
    return results
    #The program returns the list `results`, where each integer in `results` represents the number of operations required to make all elements in the corresponding array greater than the initial median of that array.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `test_cases`. Each tuple in `test_cases` contains an integer `n` and a list of `n` integers. The function returns a list `results` where each element is the number of operations required to make all elements in the corresponding array greater than the initial median of that array. The input parameters `t` and `test_cases` remain unchanged after the function execution.

