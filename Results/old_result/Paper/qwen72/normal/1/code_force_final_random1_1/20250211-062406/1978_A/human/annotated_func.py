#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of books. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: `t` is 0, `_` is a throwaway variable, `n` is an input integer, `nums` is a list of integers from the input.
#Overall this is what the function does:The function reads a series of test cases. For each test case, it reads the number of books and a list of integers representing the number of pages in each book. It then calculates and prints the sum of the maximum number of pages among all but the last book and the number of pages in the last book. After processing all test cases, the function completes without returning any value.

