#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of books. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 10^9, representing the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: t is an input integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of books. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 10^9, representing the number of pages in each book. The loop has printed the sum of the pages of the two largest books for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` representing the number of books and a list of `n` integers representing the number of pages in each book. It then sorts the list of book pages in descending order and prints the sum of the pages of the two largest books for each test case. After processing all test cases, the function concludes without returning any value.

