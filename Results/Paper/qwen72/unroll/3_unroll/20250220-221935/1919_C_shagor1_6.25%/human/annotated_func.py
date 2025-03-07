#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. For each test case, n is a positive integer (1 ≤ n ≤ 2·10^5), representing the size of the array a, and a is a list of n integers (1 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: For each test case, the variable `ans` will contain the number of integers in the array `a` that are greater than both `x` and `y` after all iterations of the inner loop have finished. The variables `x` and `y` will contain the smallest and second smallest integers in the array `a` (or `n + 1` if no such integers exist). The initial state of `t` and the sum of `n` over all test cases remains unchanged.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints the number of integers in `a` that are greater than both the smallest and the second smallest integers in the list. The function does not return any value; it only prints the result for each test case. The initial state of `t` and the sum of `n` over all test cases remains unchanged.

