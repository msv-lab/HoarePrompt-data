#State of the program right berfore the function call: T is an integer representing the number of test cases, n and k are integers where 1 ≤ k, n ≤ 2 × 10^5, and a is a list of integers of length n. Each integer in a represents the indices of the prefix or suffix maximums. The sum of the values of n across all test cases does not exceed 2 × 10^5.
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
        
    #State of the program after the  for loop has been executed: `T` is an integer representing the number of test cases, `n` is the integer value of `data[5 + T * 2 - 2]`, `k` is the integer value of `data[6 + T * 2 - 2]`, `a` is a list of integers obtained by converting `data[index:index + n]` to integers, `data` is a list of strings obtained from splitting the input string by whitespace, `MOD` is set to 10, `index` is `7 + 2 * T * 2 - 2`, `results` is a list containing either `(sum(a) % 10 + k * max_subarray_sum) % 10` or `sum(a) % 10` for each iteration, and `results` contains `T` elements, where each element is either `(sum(a) % 10 + k * max_subarray_sum) % 10` if `max_subarray_sum > 0`, or `sum(a) % 10` otherwise, and `max_subarray_sum` is the maximum sum of a contiguous subarray in `a` for each iteration.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `T` is greater than 0, `result` is the last element in `results`
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( T \), \( n \), \( k \), and a list \( a \). For each test case, it calculates a result based on the sum of the elements in \( a \) and the maximum sum of any contiguous subarray within \( a \). If the maximum sum of the subarray is positive, the result is computed as \( (\text{initial sum} + k \times \text{max subarray sum}) \mod 10^9 + 7 \); otherwise, the result is simply the initial sum modulo \( 10^9 + 7 \). The function then prints the results for each test case. Potential edge cases include invalid input values for \( T \), \( n \), and \( k \), as well as an empty list \( a \), which would result in the initial sum being returned directly without considering the maximum subarray sum. Additionally, the function assumes that the sum of \( n \) across all test cases does not exceed \( 2 \times 10^5 \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, m_1, and m_2 are integers such that 1 ≤ m_1, m_2 ≤ n ≤ 2 ⋅ 10^5, p_1, p_2, ..., p_{m_1} are integers in increasing order such that 1 ≤ p_i ≤ n, s_1, s_2, ..., s_{m_2} are integers in increasing order such that 1 ≤ s_i ≤ n, and all values of n do not exceed 2 ⋅ 10^5.
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        
        max_so_far = max(max_so_far, max_ending_here)
        
    #State of the program after the  for loop has been executed: `arr` is an array of at least 2 integers, `max_so_far` is the maximum subarray sum in `arr`, and `max_ending_here` is the maximum subarray sum ending at the last element of `arr`.
    return max_so_far
    #`The program returns max_so_far which is the maximum subarray sum in array 'arr'`
#Overall this is what the function does:The function `kadane` accepts an array `arr` of at least two integers and returns the maximum sum of any contiguous subarray within `arr`. The function iterates through the array while maintaining two variables: `max_ending_here`, which keeps track of the maximum sum of the subarray ending at the current position, and `max_so_far`, which stores the maximum sum found so far. If the current element is greater than the sum of the current element and `max_ending_here`, it means starting a new subarray at the current element could potentially yield a higher sum, so `max_ending_here` is updated to the current element. Otherwise, `max_ending_here` is updated to the sum of the current element and `max_ending_here`. After the loop, `max_so_far` contains the maximum subarray sum, which is then returned. This approach ensures that even if the array contains all negative numbers, the function correctly returns the single largest negative number as the maximum subarray sum.

