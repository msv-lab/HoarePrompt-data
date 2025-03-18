#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: Output State: `t` is a positive integer such that 0 < t ≤ 500, `_` is 3, `n` is an input integer, `nums` is a list of integers obtained from splitting the input by spaces and converting each element to an integer.
    #
    #This means that after the loop has executed all its iterations, `t` will still be a positive integer within the range of 1 to 500 (inclusive), but it will have been decremented to 0 by the end of the loop. The variable `_` will hold the value 3, indicating the last iteration of the loop. For each iteration, `n` is set to an input integer, and `nums` is a list of integers derived from another input string split by spaces and converted to integers. The loop processes each of the `t` inputs in sequence, performing the specified operation on the last two elements of the list `nums` for each input.
#Overall this is what the function does:The function processes up to 500 test cases. For each test case, it reads an integer \( n \) and a list of \( n \) integers. It then prints the sum of the second largest number and the last number in the list. After processing all test cases, the function does not return any value.

