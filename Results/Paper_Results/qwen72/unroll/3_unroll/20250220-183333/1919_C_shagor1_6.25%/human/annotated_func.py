#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2·10^5, and a is a list of integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The variable `ans` will contain the number of elements in the list `inp` that are greater than both `x` and `y` after all iterations of the loop. The values of `t`, `n`, and `inp` remain unchanged.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of integers `inp`. It then calculates the number of elements in `inp` that are greater than the two smallest distinct elements found in `inp` and prints this count. The function does not return any value, and the variables `t`, `n`, and `inp` remain unchanged after the function execution.

