#State of the program right berfore the function call: The function should accept two parameters: a list of integers `a` representing the number of pages in each book, and an integer `n` representing the number of books, such that 2 <= n <= 100 and 1 <= a_i <= 10^9 for all 1 <= i <= n. The function should be called multiple times for different test cases, with the number of test cases `t` being an integer such that 1 <= t <= 500.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The loop has executed `t` times, and for each iteration, it has read an integer `n` and a list of integers `nums` from the input. It then printed the sum of the maximum value in the list `nums` (excluding the last element) and the last element of the list `nums`. The variables `t`, `n`, and `nums` are not retained between iterations, so they will be reset for each new test case. The initial list `a` and the integer `n` from the initial state are not modified by the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums` from the input. It then prints the sum of the maximum value in the list `nums` (excluding the last element) and the last element of the list `nums`. The function does not return any value; it only prints the result for each test case. The variables `t`, `n`, and `nums` are reset for each test case, and the function does not modify any external variables or state.

