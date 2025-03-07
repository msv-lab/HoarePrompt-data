#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `tc` is equal to 0, `i` is equal to `n-1`, `n` is the length of `arr` minus 1, `arr` is a list of integers in descending order with 0 appended as the last element, `dp` is the final result of applying the condition `arr[i] - arr[i + 1] > 1 or not dp` iteratively from `i = 1` to `i = n-1`.
    #
    #Explanation: After all iterations of the loop have finished, `tc` will be reduced to 0 since it starts as the initial value of `tc` and is decremented by 1 in each iteration. The variable `i` will be `n-1` because the loop runs until `i` reaches `n-1`. The variable `n` will be the length of `arr` minus 1, as `n` is set to `len(arr) - 1` at the beginning of each iteration. The list `arr` remains sorted in descending order with 0 appended at the end. The boolean variable `dp` will hold the final result of the condition evaluated over all iterations, starting from `i = 1` up to `i = n-1`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( n \) and a list of \( n \) integers. It then sorts these integers in descending order, appends a zero at the end, and checks if the difference between consecutive elements is greater than 1 or if the previous result was false. Based on this check, it prints either "Alice" or "Bob". After processing all test cases, the function ensures that the number of test cases processed (`tc`) is zero.

