#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the number of books. This is followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) where each integer represents the number of pages in each book. The number of test cases t (1 ≤ t ≤ 500) is given at the beginning of the input.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: `t` is an integer representing the number of test cases and must be 0; no more iterations will execute.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of books and the number of pages in each book. For each test case, it calculates the sum of the pages of all books except the last one, adds the number of pages in the last book, and prints this total.

