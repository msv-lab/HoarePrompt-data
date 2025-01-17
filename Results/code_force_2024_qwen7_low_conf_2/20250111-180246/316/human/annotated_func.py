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
        
    #State of the program after the  for loop has been executed: `t` is 0, `n` is the last input integer processed, `a` is the last second input integer processed, `b` is the last third input integer processed, `c` is the last `a * n`, `d` is the last `b + (n - 2) * a`, `e` is the minimum of `a`, `c`, and `d`, and `e` is printed.
#Overall this is what the function does:- The function assumes that `t` is always positive and within the given range (`1 ≤ t ≤ 10^4`). If `t` is outside this range, the function may behave unpredictably.
- The function does not handle invalid input types (e.g., non-integer inputs) or invalid ranges for `n`, `a`, and `b`.
- There is no error handling for cases where `n` might be 0, although this scenario is technically covered by the condition `n == 1` which assigns `a` directly to `e`.

