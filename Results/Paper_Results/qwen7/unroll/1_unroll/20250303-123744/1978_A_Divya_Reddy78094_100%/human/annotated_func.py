#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), and it is now set to the value it was after all iterations of the loop; n is an unknown integer between 2 and 100 (inclusive), and it is now set to the value it was during the last iteration of the loop; nums is a list of integers representing the number of pages in each book for the last iteration of the loop; the value of max(nums[:-1]) + nums[-1] from the last iteration of the loop is printed.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer t indicating the number of test cases, an integer n indicating the number of books, and a list of n integers representing the number of pages in each book. It then prints the sum of the maximum page number of all but the last book and the page number of the last book for each test case.

