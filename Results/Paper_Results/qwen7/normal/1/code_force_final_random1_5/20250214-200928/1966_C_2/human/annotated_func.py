#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each pile i, and the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: Output State: `tc` is `0`; `i` is `n`; `dp` is a boolean value determined by the final iteration's condition `arr[n-1] - arr[n] > 1`.
    #
    #Explanation: After all iterations of the loop have finished, `tc` will be reduced to `0` because it starts as `tc` and decreases by `1` in each iteration until it reaches `0`. The variable `i` will be equal to `n` because the loop ends before incrementing `i` again. The value of `dp` will be the result of the final condition check in the loop, which is `arr[n-1] - arr[n] > 1` (since `arr` is extended with a `0` and `n` is set to `len(arr) - 1`).
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a positive integer \( n \) and a list of \( n \) integers. It then sorts and modifies this list, checks a specific condition related to consecutive elements in the list, and prints either "Alice" or "Bob" based on the result of this condition. After processing all test cases, the function ensures that the number of remaining test cases (`tc`) is zero.

