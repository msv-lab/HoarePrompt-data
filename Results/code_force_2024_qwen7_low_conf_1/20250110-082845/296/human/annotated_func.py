#State of the program right berfore the function call: n is an integer representing the length of the permutation, k is an integer representing the number of prefix maximums, and a is a list of integers representing the indices of the prefix maximums. Additionally, there is another list of integers representing the indices of the suffix maximums, which is not provided in the function signature but is part of the problem description.
def func_1():
    input = sys.stdin.read
    data = input().split()
    MOD = 10 ** 9 + 7
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n, k = int(data[index]), int(data[index + 1])
        
        index += 2
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        initial_sum = sum(a) % MOD
        
        max_subarray_sum = kadane(a)
        
        if max_subarray_sum > 0:
            result = (initial_sum + k * max_subarray_sum) % MOD
        else:
            result = initial_sum % MOD
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `T` is 0, `a` is a list of integers representing the indices of the prefix maximums for each iteration, `k` is an integer representing the number of prefix maximums for each iteration, `index` is the final position in the `data` list after processing all iterations, `initial_sum` is the sum of `a` modulo `MOD` for each iteration, `max_subarray_sum` is the maximum subarray sum of `a` as calculated by Kadane's algorithm for each iteration, `result` is `(initial_sum + k * max_subarray_sum) % MOD` if `max_subarray_sum > 0`; otherwise, `result` is `initial_sum % MOD` for each iteration, and `results` is a list containing all the `result` values.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `results` is a list containing the results of all iterations, and the loop prints each element of `results` in sequence.
#Overall this is what the function does:The function processes multiple test cases, each defined by the length of a permutation \( n \), the number of prefix maximums \( k \), and a list \( a \) of integers representing the indices of the prefix maximums. For each test case, it calculates the sum of the elements in \( a \) modulo \( 10^9 + 7 \), finds the maximum subarray sum using Kadane’s algorithm, and computes the final result based on whether the maximum subarray sum is positive or zero. If the maximum subarray sum is positive, the result is the initial sum plus \( k \) times the maximum subarray sum, all modulo \( 10^9 + 7 \). Otherwise, the result is just the initial sum modulo \( 10^9 + 7 \). The function then appends each computed result to a list and prints all results in sequence. Potential edge cases include scenarios where the input list \( a \) is empty or contains only negative numbers, leading to a maximum subarray sum of zero.

#State of the program right berfore the function call: arr is a list of integers representing the sequence of prefix and suffix maximums indices.
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        
        max_so_far = max(max_so_far, max_ending_here)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `max_so_far` is the maximum subarray sum in the list `arr`, `max_ending_here` is the maximum sum of subarrays ending at the current position for each element in `arr`.
    return max_so_far
    #The program returns `max_so_far`, which is the maximum subarray sum in the list `arr`
#Overall this is what the function does:The function `kadane` accepts a list of integers `arr` and computes the maximum sum of any contiguous subarray within the list. It iterates through the list while maintaining two variables: `max_ending_here`, which tracks the maximum subarray sum ending at the current position, and `max_so_far`, which keeps track of the overall maximum subarray sum encountered during the iteration. The function returns `max_so_far`, which represents the maximum subarray sum in the list. Potential edge cases include an empty list, where the function should return 0, and a list with all negative numbers, where the function should return the largest negative number.

