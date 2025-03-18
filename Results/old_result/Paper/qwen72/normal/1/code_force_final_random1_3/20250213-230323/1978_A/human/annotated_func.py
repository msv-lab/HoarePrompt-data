#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of books. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: `t` is an integer input by the user within the range 1 ≤ t ≤ 500, `n` is an input integer, `a` is a list of n integers where 1 ≤ a_i ≤ 10^9, `_` has iterated `t` times, `nums` is a list of integers provided by the user, and the loop has completed all its iterations.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list of `n` integers representing the number of pages in each book. For each test case, the function calculates the sum of the maximum value among the first `n-1` books and the last book's page count, then prints this sum. After processing all test cases, the function completes without returning any value. The state of the program after the function concludes includes the completion of all iterations over the test cases, with the results printed to the standard output.

