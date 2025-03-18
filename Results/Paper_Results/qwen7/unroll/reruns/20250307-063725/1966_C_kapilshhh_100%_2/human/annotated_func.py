#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will be a series of strings either "Alice" or "Bob", each corresponding to the result of one iteration of the loop based on the input provided during that iteration.
    #
    #Explanation: During each iteration of the loop, the program reads an integer `n`, then a list of integers from the user input. It processes this list to determine whether Alice or Bob wins based on a specific condition involving the difference between consecutive elements in the sorted, unique list. The result ("Alice" or "Bob") is printed, and `tc` (which represents the number of test cases) is decremented. After all iterations are complete, the final output consists of these results printed in sequence.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers representing the number of stones in each pile. It then sorts and processes this list to determine whether Alice or Bob wins based on a specific condition involving the difference between consecutive elements in the sorted, unique list. The function prints "Alice" or "Bob" for each test case, indicating the winner. After processing all test cases, it outputs a series of "Alice" or "Bob" results in sequence.

