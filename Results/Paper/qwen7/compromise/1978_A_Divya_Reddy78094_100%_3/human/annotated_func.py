#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), and for each iteration of the loop, `n` is an integer read from input, `nums` is a list of integers read from input and split, and the output is the result of `max(nums[:-1]) + nums[-1]`. After all iterations, the value of `t` remains the same, but the values of `n` and `nums` change with each iteration based on user input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (number of books), and a list of \( n \) integers representing the number of pages in each book. For each test case, it calculates and prints the sum of the maximum page count of the first \( n-1 \) books and the last book. After processing all test cases, it outputs the results for each case.

