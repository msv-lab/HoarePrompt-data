#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: `t` must be greater than 0, `_` is `t-1`, `n` is an input integer, `nums` is a list of integers sorted in descending order.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the input, sorts the list in descending order, and prints the sum of the two largest integers in the list. The function does not return any value; it only prints the results. After the function concludes, `t` is the number of test cases, `_` is the loop counter (which will be `t-1` after the last iteration), `n` is the last input integer, and `nums` is the last sorted list of integers.

