#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. v is a list of n integers where 1 ≤ v[i] ≤ 10^9 for each 0 ≤ i < n. x is a list of n integers where -n ≤ x[i] < x[i + 1] ≤ n for each 0 ≤ i < n - 1 and x[i] ≠ 0.
def func_1():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    x = list(map(int, input().split()))
    put_all_on_right = [0] * (n + 1)
    for i in range(n):
        put_all_on_right[abs(x[i])] += v[i]
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `k` is an integer, `v` is a list of `n` integers where each element is between 1 and \(10^9\), `x` is a list of integers where \(-n \leq x[i] < x[i+1] \leq n\) for each \(0 \leq i < n-1\) and \(x[i] \neq 0\), `put_all_on_right` is a list of length `n + 1` where each element is the sum of `v[i]` for all `i` such that \(|x[i]| = j\) for \(0 \leq j \leq n\)
    my_power = k
    for i in range(1, n + 1):
        if my_power < put_all_on_right[i]:
            print('NO')
            return
        
        my_power -= put_all_on_right[i]
        
        my_power += k
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is a non-negative integer, `my_power` is the original value of `my_power` plus `k` times `n` minus the sum of `put_all_on_right[i]` for all `i` in the range `[1, n]`.
    print('YES')
#Overall this is what the function does:The function `func_1` takes no parameters but reads three lists (`n`, `k`, and `v`) and a list (`x`) from standard input. It then calculates the sum of elements in `v` for each absolute position specified by `x`. If at any point the power (`my_power`) is less than the calculated sum for a given position, it prints 'NO' and exits. Otherwise, it continues reducing `my_power` by these sums and adding `k` to `my_power` at each step. If it completes the loop without finding a case where `my_power` is insufficient, it prints 'YES'. The function returns `None` in both cases where it prints 'NO' or 'YES'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3⋅10^4. Each test case consists of three lines where the first line contains two integers n and k such that 1 ≤ n ≤ 3⋅10^5 and 1 ≤ k ≤ 2⋅10^9. The second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The third line contains n integers x_1, x_2, ..., x_n such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0. The sum of n over all test cases does not exceed 3⋅10^5.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` processes a series of test cases. Each test case consists of integers \( n \) and \( k \), followed by two lists of \( n \) integers \( a_i \) and \( x_i \). The function calls another function `func_1` for each test case. After processing all test cases, the function does not return any value. The state of the program after the function concludes is that `func_1` has been called \( t \) times, where \( t \) is the number of test cases. The function does not provide any output or return any results; it only processes the input data and calls `func_1` for each test case.

