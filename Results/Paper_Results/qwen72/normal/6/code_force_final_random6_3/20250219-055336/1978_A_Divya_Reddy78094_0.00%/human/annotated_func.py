#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 500), the number of test cases, and a list of lists, where each inner list contains n (2 ≤ n ≤ 100) integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9), representing the number of pages in each book for each test case.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: `t` must be greater than 0, `_` is `t-1`, `n` is the last input integer, `nums` is a list of integers input by the user, sorted in descending order.
#Overall this is what the function does:The function `func` takes no parameters and reads input from the user. It processes `t` test cases, where `t` is an integer provided by the user (1 ≤ t ≤ 500). For each test case, it reads an integer `n` (2 ≤ n ≤ 100) representing the number of books, and a list of `n` integers representing the number of pages in each book. The function sorts the list of pages in descending order and prints the sum of the two largest page counts for each test case. The function does not return any value. After the function concludes, `t` test cases have been processed, and the sum of the two largest page counts for each test case has been printed.

