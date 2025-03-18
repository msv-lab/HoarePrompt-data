#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains n (2 ≤ n ≤ 100) integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of pages in each book for a test case.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: `t` must be greater than 0, `_` is `t-1`, `n` is an input integer, `nums` is a list of integers input by the user, sorted in descending order.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the input, sorts the list in descending order, and prints the sum of the two largest integers in the list. The function does not return any value. After the function concludes, `t` test cases have been processed, and for each test case, the sum of the two largest integers in the input list has been printed.

