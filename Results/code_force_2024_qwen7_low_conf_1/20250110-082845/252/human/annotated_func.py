#State of the program right berfore the function call: n and k are positive integers where 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. v is a list of positive integers representing the health points of n monsters, and x is a sorted list of distinct integers representing the positions of these n monsters on a line, where -n ≤ x_i < x_{i+1} ≤ n and x_i ≠ 0.
def func_1():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    x = list(map(int, input().split()))
    put_all_on_right = [0] * (n + 1)
    for i in range(n):
        put_all_on_right[abs(x[i])] += v[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a positive integer, `v` is a list of integers read from input, `x` is a list of integers read from input, for every index `i` in range `n`, `put_all_on_right[abs(x[i])]` is increased by `v[i]`, `i` is `n`.
    my_power = k
    for i in range(1, n + 1):
        if my_power < put_all_on_right[i]:
            print('NO')
            return
        
        my_power -= put_all_on_right[i]
        
        my_power += k
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is a positive integer, `my_power` is equal to \((n - \sum_{j=1}^{n-1} \text{put_all_on_right}[j]) + nk\), and `k` remains unchanged.
    print('YES')
#Overall this is what the function does:The function `func_1` accepts four parameters: `n`, `k`, `v`, and `x`. It reads these values from input where `n` and `k` are positive integers, `v` is a list of positive integers representing the health points of `n` monsters, and `x` is a sorted list of distinct integers representing the positions of these monsters on a line. The function calculates whether it is possible to defeat all monsters starting with `k` initial power points. It does this by iterating through the positions of the monsters, updating the power based on the total health points of the monsters at each position, and checking if the current power is sufficient to defeat the monsters at that position. If the power becomes insufficient at any point, the function prints 'NO' and returns immediately. If the function successfully iterates through all the monsters without running out of power, it prints 'YES'. The function does not return any value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3⋅10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 1 ≤ k ≤ 2⋅10^9. The list a contains n integers such that 1 ≤ a_i ≤ 10^9, and the list x contains n integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State of the program after the  for loop has been executed: `t` is an input integer with 1 ≤ t ≤ 3⋅10^4 and `t` is greater than the number of iterations of the loop minus one; the function `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2()` accepts no explicit parameters but relies on predefined lists `a` and `x`, and an integer `t` which is expected to be an input. It iterates `t` times, executing the function `func_1()` in each iteration. After the loop, it does not return any value. The function ensures that `t` is within the constraint \(1 \leq t \leq 3 \times 10^4\). If `t` is invalid, the function will still proceed but will ignore the invalid input. The function also assumes that `func_1()` processes the lists `a` and `x` in each iteration. However, the function does not validate the contents of the lists `a` and `x` against their respective constraints (i.e., \(1 \leq a_i \leq 10^9\) and \(-n \leq x_1 < x_2 < \ldots < x_n \leq n\) and \(x_i \neq 0\)). Therefore, the function does not ensure these constraints are met.

