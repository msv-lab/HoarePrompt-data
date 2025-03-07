#State of the program right berfore the function call: The function should accept two parameters: `t` (an integer representing the number of test cases, where 1 ≤ t ≤ 500) and a list of lists `cases` where each inner list represents a test case. Each test case list contains an integer `n` (where 2 ≤ n ≤ 100) followed by `n` integers `a_1, a_2, ..., a_n` (where 1 ≤ a_i ≤ 10^9) representing the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: `t` must be equal to the initial value of `t`, `_` is `t-1`, `n` is an input integer, `nums` is a list of integers from the last input.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads an integer `n` followed by `n` integers representing the number of pages in each book. It then calculates and prints the sum of the maximum of the first `n-1` numbers and the last number. The function does not return any value; it only prints the results to the standard output. After the function completes, the input values `t`, `n`, and `nums` will reflect the state of the last test case processed.

