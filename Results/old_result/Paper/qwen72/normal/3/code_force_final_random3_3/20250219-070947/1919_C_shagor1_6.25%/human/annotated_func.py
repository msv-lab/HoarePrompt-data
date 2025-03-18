#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `_` is `t - 1`, `inp` is a new list of integers from the input that must have at least 1 element, `a` is the last element of `inp`, `x` is the smallest element in `inp`, `y` is the second smallest element in `inp` (if it exists, otherwise `y` is `n + 1`), and `ans` is the number of elements in `inp` that are greater than both `x` and `y` after all iterations.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers `inp`. It then calculates the number of elements in `inp` that are greater than both the smallest and the second smallest elements in `inp`. This count is printed for each test case. The function does not return any value, but it modifies the state of the program by printing the result for each test case. After the function concludes, `t` is unchanged, `_` is `t - 1`, `inp` contains the last list of integers read, `a` is the last element of `inp`, `x` is the smallest element in `inp`, `y` is the second smallest element in `inp` (or `n + 1` if there is no second smallest element), and `ans` is the count of elements greater than both `x` and `y`.

