#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if n == 1:
            e = a
        else:
            c = a * n
            d = b + (n - 2) * a
            e = min(c, d)
        
        print(e)
        
    #State of the program after the  for loop has been executed: `t` is 0, `n`, `a`, and `b` are integers obtained from the input split when `t` was greater than 0, `c` is the product of `a` and `n`, `d` is the sum of `b` and `(n - 2) * a`, and `e` is the minimum of `c` and `d`, `e` is printed for each iteration.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads three integers `n`, `a`, and `b` from input. If `n` is 1, it sets `e` to `a`. Otherwise, it calculates `c` as the product of `a` and `n`, and `d` as the sum of `b` and `(n - 2) * a`. Then, it sets `e` to the minimum of `c` and `d`. Finally, it prints `e` for each test case. After processing all test cases, the function does not return anything explicitly; however, it outputs the value of `e` for each test case. Potential edge cases include when `n` is 1 or when `t` is 0 (though the latter would result in no output). There is no missing functionality noted in the provided code.

