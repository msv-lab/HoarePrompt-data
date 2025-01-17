#State of the program right berfore the function call: T is an integer representing the number of test cases; n, k are integers such that 1 ≤ k, n ≤ 2 ⋅ 10^5; a is a list of integers where 1 ≤ a_i ≤ n; the sum of the values of n across all test cases does not exceed 2 ⋅ 10^5; the list a has length equal to n; and max_subarray_sum is a function that returns the maximum subarray sum using Kadane's algorithm applied to the list a.
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
        
    #State of the program after the  for loop has been executed: `T` is 0, `MOD` is 1000000007, `results` is a list containing the results computed for each iteration, `index` is the original value of `index` + the sum of `n` for all iterations, `data` is unchanged, `a` is a list of integers created from `data[index:index + n]` for each iteration, `initial_sum` is the sum of `a` modulo `MOD` for each iteration, `max_subarray_sum` is the maximum subarray sum computed using Kadane's algorithm for each iteration, `result` is `(initial_sum + k * max_subarray_sum) % MOD` if `max_subarray_sum` > 0, otherwise `result` is `initial_sum % MOD` for each iteration.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `results` contains the results computed for each iteration of the loop, each `result` in `results` is either `(initial_sum + k * max_subarray_sum) % MOD` if `max_subarray_sum` > 0, otherwise `result` is `initial_sum % MOD`, where `initial_sum` is the sum of `a` modulo `MOD` for each iteration, `max_subarray_sum` is the maximum subarray sum computed using Kadane's algorithm for each iteration, `k` is the number of iterations, and `MOD` is 1000000007.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( k \), and a list \( a \) of \( n \) integers. It calculates the initial sum of the elements in \( a \) modulo \( 10^9 + 7 \). Then, it finds the maximum subarray sum of \( a \) using Kadane's algorithm. If the maximum subarray sum is positive, the function computes the result as \( (\text{initial sum} + k \times \text{max subarray sum}) \mod (10^9 + 7) \); otherwise, it simply takes the initial sum modulo \( 10^9 + 7 \). The function collects these results for all test cases and prints them. The function handles up to \( 2 \times 10^5 \) elements across all test cases.

#State of the program right berfore the function call: arr is a list of integers.
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        
        max_so_far = max(max_so_far, max_ending_here)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `max_so_far` is the maximum subarray sum starting from the beginning of the array up to any index, `max_ending_here` is the maximum subarray sum ending at the current index, and `x` is the last element in the array that was processed during the loop.
    return max_so_far
    #`The program returns max_so_far, which is the maximum subarray sum starting from the beginning of the array up to any index`
#Overall this is what the function does:The function `kadane` accepts a list of integers `arr` and computes the maximum sum of any contiguous subarray within the input list. It returns this maximum subarray sum. The function iterates through the list while maintaining two variables: `max_ending_here`, which keeps track of the maximum subarray sum ending at the current position, and `max_so_far`, which stores the maximum subarray sum found so far. If the current element alone is greater than the sum of the current element and `max_ending_here`, then `max_ending_here` is updated to the current element. Otherwise, `max_ending_here` is updated to the sum of the current element and `max_ending_here`. The function also handles edge cases such as when all elements in the list are negative, in which case `max_so_far` will be the largest (least negative) number in the list.

