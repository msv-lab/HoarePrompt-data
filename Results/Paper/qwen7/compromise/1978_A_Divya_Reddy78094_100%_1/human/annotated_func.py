#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), and for each iteration of the loop, `n` is an integer read from input, `nums` is a list of integers obtained by splitting another input string, and the loop prints the sum of the second largest number in `nums` and the last number in `nums`. After all iterations, the value of `t` remains unchanged, but the printed outputs are the sums calculated for each input list `nums`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) indicating the number of test cases, followed by an integer \( n \) and a list of \( n \) integers representing the number of pages in each book. For each test case, it calculates and prints the sum of the second largest number and the last number in the list of pages. The function does not return any value but produces output for each test case.

