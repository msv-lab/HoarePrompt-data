#State of the program right berfore the function call: n and k are integers where 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9, v is a list of n integers where 1 ≤ v_i ≤ 10^9, and x is a list of n integers where -n ≤ x_i < x_{i+1} ≤ n and x_i ≠ 0.
def func_1():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    x = list(map(int, input().split()))
    put_all_on_right = [0] * (n + 1)
    for i in range(n):
        put_all_on_right[abs(x[i])] += v[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 3 \cdot 10^5\), `k` is an integer where \(1 \leq k \leq 2 \cdot 10^9\), `v` is a list of \(n\) integers where \(1 \leq v_i \leq 10^9\), `x` is a list of integers read from the input, `put_all_on_right` is a list of \(n + 1\) integers, where for each index \(i\), `put_all_on_right[i]` is the sum of `v[j]` for all \(j\) such that `abs(x[j]) = i`.
    my_power = k
    for i in range(1, n + 1):
        if my_power < put_all_on_right[i]:
            print('NO')
            return
        
        my_power -= put_all_on_right[i]
        
        my_power += k
        
    #State of the program after the  for loop has been executed: `my_power` is equal to the original value of `my_power` minus the sum of all `put_all_on_right[i]` for `i` from 1 to `n` plus `n * k`.
    print('YES')
#Overall this is what the function does:The function reads three lists `n`, `k`, `v`, and `x` from the standard input, where `n` is the number of elements, `k` is an integer, `v` is a list of integers, and `x` is a list of integers representing positions. It then calculates a list `put_all_on_right` which stores the sum of values in `v` corresponding to the absolute values in `x`. After that, it checks whether `my_power` (initially set to `k`) can handle the sums in `put_all_on_right` by decrementing `my_power` by each value in `put_all_on_right` and then adding `k` back. If `my_power` becomes less than any value in `put_all_on_right`, it prints 'NO' and returns. Otherwise, it prints 'YES'. The function does not return anything and operates based on the input provided.

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 3⋅10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 1 ≤ k ≤ 2⋅10^9. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 10^9, and x_1, x_2, ..., x_n are integers where -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State of the program after the  for loop has been executed: `t` is an integer representing the number of test cases, where \(1 \leq t \leq 3 \cdot 10^4\).
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \(n\) and \(k\), along with two lists of integers \(a_1, a_2, \ldots, a_n\) and \(x_1, x_2, \ldots, x_n\). It then calls a function `func_1()` for each test case to process these inputs. After executing the loop, the function returns nothing (i.e., it does not return any value). The function accepts an integer `t` representing the number of test cases, where \(1 \leq t \leq 3 \cdot 10^4\). There are no explicit postconditions mentioned for the function itself, and the return postconditions indicate that the function does not return any value. However, it is implied that `func_1()` should process the inputs for each test case according to its specifications.

