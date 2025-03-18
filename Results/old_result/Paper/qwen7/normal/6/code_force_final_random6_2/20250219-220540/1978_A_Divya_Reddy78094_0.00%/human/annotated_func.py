#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: Output State: `t` is an integer between 1 and 497 (inclusive), `n` is an input integer, `nums` is a list of integers sorted in descending order after sorting.
    #
    #This output state occurs because the loop runs `t` times, and since `t` ranges from 1 to 500 initially, after running the loop 500 times, `t` will be reduced by 500 - 3 = 497. The values of `n` and the list `nums` remain as they are after each iteration of the loop, with `n` being an input integer and `nums` being a list of integers sorted in descending order after sorting.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t (number of test cases) and for each test case, an integer n (number of books) and a list of n integers representing the number of pages in each book. The function sorts the list of pages in descending order for each test case and prints the sum of the pages of the two books with the most pages. After processing all test cases, the function does not return any value but outputs the sum of the pages for each test case.

