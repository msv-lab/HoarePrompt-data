#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` representing the number of pages in each book, and an integer `n` representing the number of books, where 2 ≤ n ≤ 100 and 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. However, the provided function definition does not include these parameters. The correct function definition should be: `def func(a, n):`.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The loop will execute `t` times, and for each iteration, it will read an integer `n` and a list of `n` integers `nums`. It will then print the sum of the maximum of the first `n-1` elements in `nums` and the last element in `nums`. The variables `a` and `n` from the initial state remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums`. It then prints the sum of the maximum of the first `n-1` elements in `nums` and the last element in `nums`. The function does not return any value and does not modify any external state or variables.

