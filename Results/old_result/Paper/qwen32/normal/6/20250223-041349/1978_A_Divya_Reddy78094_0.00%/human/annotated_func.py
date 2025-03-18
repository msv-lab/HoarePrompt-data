#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the number of books. This is followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) where each integer represents the number of pages in each book. The first line of the input contains a single integer t (1 ≤ t ≤ 500) indicating the number of test cases.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: `t` is an input integer representing the number of test cases, where 0 ≤ t ≤ 500; all test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of books and the number of pages in each book. It outputs the sum of the pages of the two books with the most pages for each test case.

