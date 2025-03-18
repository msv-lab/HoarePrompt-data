#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: Output State: `t` is greater than 0 and an integer between 1 and 1 (inclusive), `n` is an input integer, `nums` is a list of integers obtained from splitting the input string and converting each element to an integer.
    #
    #In natural language: After the loop has executed all its iterations, `t` will be reduced to 1 and then decremented to 0, meaning the loop condition `t > 0` will no longer be true. Therefore, the loop will stop executing. At this point, `t` will be 0, which is still within the range of 1 to 1 (inclusive), `n` will be the last input integer received, and `nums` will be the list of integers from the last input string split and converted.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (number of books), and a list of n integers representing the number of pages in each book. For each test case, it calculates and prints the sum of the maximum page count of the first n-1 books and the page count of the last book. After processing all test cases, the function does not return any value.

