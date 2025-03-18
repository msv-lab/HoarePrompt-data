#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After the loop executes all iterations, `x` will be the smallest element in `inp`, `y` will be the second smallest element in `inp` (if it exists, otherwise `y` will be `n + 1`), and `ans` will be the count of elements in `inp` that are greater than both `x` and `y`. The value of `n` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list `a` of `n` integers. For each test case, it identifies the smallest and second smallest elements in `a` (if they exist) and counts how many elements in `a` are greater than both of these elements. The function prints the count for each test case and does not return any value. The state after the function concludes is that the smallest element in `a` is stored in `x`, the second smallest element (if it exists) is stored in `y`, and `ans` contains the count of elements greater than both `x` and `y`. The value of `n` remains unchanged for each test case.

