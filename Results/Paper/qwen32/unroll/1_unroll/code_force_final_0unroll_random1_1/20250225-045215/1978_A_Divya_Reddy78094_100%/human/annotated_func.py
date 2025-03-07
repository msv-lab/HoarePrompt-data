#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the number of books. This is followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of pages in each book. The first line of the input contains a single integer t (1 ≤ t ≤ 500) indicating the number of test cases.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The value of `t` remains unchanged as it represents the number of test cases. For each test case, the program reads the number of books `n` and the list of integers `a_1, a_2, ..., a_n`. It then calculates and prints the sum of the maximum value from all but the last integer in the list and the last integer itself. No other variables are changed beyond the loop's iteration counter and the input values read within each iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the number of books and a list of `n` integers representing the number of pages in each book. For each test case, it calculates and prints the sum of the maximum number of pages from the first `n-1` books and the number of pages in the last book.

