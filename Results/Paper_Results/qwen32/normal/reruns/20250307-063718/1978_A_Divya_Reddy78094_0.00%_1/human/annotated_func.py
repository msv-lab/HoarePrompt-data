#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains a single integer n (2 ≤ n ≤ 100) representing the number of books. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of pages in each book. The total number of test cases t is between 1 and 500.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 500; the loop has executed `t` times; for each iteration, `n` is an input integer, and `nums` is a list of integers sorted in descending order, and the sum of the two largest numbers in `nums` has been printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of books and the number of pages in each book. For each test case, it outputs the sum of the pages of the two books with the most pages.

