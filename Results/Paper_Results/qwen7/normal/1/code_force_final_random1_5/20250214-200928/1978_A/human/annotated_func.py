#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: Output State: `t` is less than or equal to 0, or `t` is a non-negative integer, `n` is an input integer, `nums` is a list of integers obtained from splitting the input string by spaces and converting each element to an integer for each iteration.
    #
    #In natural language: After the loop has executed all its iterations, `t` must be less than or equal to 0 because the loop runs `t` times, and once `t` becomes 0 or negative, the loop stops executing. At this point, `n` will be the last input integer received during any of the iterations, and `nums` will be the list of integers corresponding to the last input string split and converted to integers.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t indicating the number of books, followed by an integer n and a list of n integers representing the number of pages in each book. For each test case, the function calculates and prints the sum of the maximum page count of the first n-1 books and the page count of the last book. After processing all test cases, the function does not return any value.

