#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `tc` is less than or equal to 0, `n` is 0, `arr` is a list containing unique, sorted integers in descending order followed by 0, `dp` is `arr[0] - arr[1] > 1 or not dp`, `i` is equal to 0.
    #
    #Explanation: After all iterations of the loop have finished, `tc` will be less than or equal to 0 because it is decremented by 1 in each iteration until it becomes 0 or negative. The variable `n` will be 0 since it is set to `len(arr) - 1`, and `len(arr)` will be 1 when `arr` contains only one element (which is the last 0). The variable `i` will also be 0 as it starts from 1 and reaches the end of the list in the last iteration, but since the list has only one element, `i` will never be incremented beyond 0. The value of `dp` will be determined by the condition `arr[0] - arr[1] > 1 or not dp`, where `arr[1]` is 0, so the condition simplifies to `arr[0] > 1 or not dp`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t indicating the number of test cases, followed by n integers representing the number of stones in each pile. For each test case, it sorts and processes the unique stones in descending order. It then determines whether Alice or Bob wins based on specific conditions involving the differences between consecutive stones. The function prints either "Alice" or "Bob" for each test case. After processing all test cases, the function ends with all relevant variables reset or updated according to the final state of the loop.

