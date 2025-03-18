#State of the program right berfore the function call: a is a list of non-negative integers representing the health of the monsters, x is a list of integers representing the initial positions of the monsters, and k is a non-negative integer representing the number of bullets you can fire per second. The length of a and x is n, and the values in x are sorted in strictly increasing order and none of them are zero.
def func_1(a, x, k):
    n = len(a)
    sorted_indices = sorted(range(n), key=lambda i: abs(x[i]))
    distance = 0
    pos = 0
    while pos != len(sorted_indices):
        if abs(x[sorted_indices[pos]]) == distance:
            return False
        
        rest = k
        
        while rest != 0 and pos != len(sorted_indices):
            delta = min(rest, a[sorted_indices[pos]])
            rest -= delta
            a[sorted_indices[pos]] -= delta
            if a[sorted_indices[pos]] == 0:
                pos += 1
        
        distance += 1
        
    #State: Output State: `distance` is increased by a total of 10 units (2 units per iteration for the first 5 iterations, and 1 unit per iteration for the next 5 iterations), `pos` is either equal to `len(sorted_indices)` or one less than it (depending on whether `a[sorted_indices[pos]]` became zero before `rest` reached 0), and each element in `a` that was targeted by the loop has been decremented by its respective `delta` value. If an element in `a` was reduced to zero, it was skipped in subsequent iterations. The exact values of `a[sorted_indices[pos]]` will depend on how many times each index was decremented during the loop's execution. The `rest` variable will be reduced to 0 after all iterations, and no further changes will occur to `distance` or `pos` beyond the 10th iteration.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts three parameters: a list of non-negative integers `a`, a list of integers `x`, and a non-negative integer `k`. The length of `a` and `x` is `n`, and the values in `x` are sorted in strictly increasing order with no zeros. The function attempts to reduce the elements in list `a` by firing bullets according to the positions in list `x` and the rate specified by `k`. If at any point, the absolute position in `x` matches the current distance, the function returns `False`. Otherwise, after up to 10 iterations, the function returns `True`.

#State of the program right berfore the function call: t is an integer representing the number of test cases; n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9; a is a list of n integers where 1 ≤ a_i ≤ 10^9; x is a list of n integers where -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: Output State: `t` must be equal to the total number of iterations the loop executed, `n` is the last integer input converted to an integer obtained from the final iteration of the loop, `k` is the last integer input converted to an integer obtained from the final iteration of the loop, `a` is a list of integers obtained from the final input split and converted using `map(int, input().split())` for the last iteration, `x` is a list of integers obtained from the final input split and converted using `map(int, input().split())` for the last iteration.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will be the total number of iterations (which is the value it was set to at the start), `n` and `k` will be the values they were given in the last iteration of the loop, and `a` and `x` will be the lists of integers provided as inputs in the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n and k, followed by lists a and x. It then calls another function `func_1` with these inputs and prints 'YES' if `func_1` returns True, otherwise it prints 'NO'. After processing all test cases, the function outputs the results for each case.

