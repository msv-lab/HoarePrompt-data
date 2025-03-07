#State of the program right berfore the function call: a is a list of non-negative integers representing the health of the monsters, x is a list of integers representing the initial positions of the monsters, and k is a non-negative integer representing the number of bullets that can be fired per second. The length of a and x is n, where 1 <= n <= 3 * 10^5, and 1 <= k <= 2 * 10^9. The values in x are sorted in ascending order and are non-zero, with -n <= x[i] < x[i+1] <= n for all i.
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
        
    #State: Output State: `distance` is equal to the maximum value found in the list `x` plus 1, `pos` is equal to `len(sorted_indices)`, `rest` is 0, and all values in the list `a` indexed by `sorted_indices` are reduced to 0 or remain unchanged based on the deductions made during the loop iterations.
    #
    #This output state is derived from the understanding that the loop continues to increment `distance` until all elements in the list `a` indexed by `sorted_indices` are reduced to 0. The variable `pos` reaches the end of `sorted_indices` once all elements have been processed. The `rest` variable starts fresh at the beginning of each outer loop iteration but is eventually reduced to 0 as it is used to decrement the values in `a`. The `distance` variable increases with each full cycle of the outer loop, stopping when the condition to exit the loop is met.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts three parameters: a list of non-negative integers `a` representing the health of the monsters, a list of integers `x` representing the initial positions of the monsters, and a non-negative integer `k` representing the number of bullets that can be fired per second. It returns `True` if it can reduce the health of all monsters to zero using the given number of bullets per second, otherwise it returns `False`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4; n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9; a is a list of n integers such that 1 ≤ a_i ≤ 10^9; x is a list of n integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: Output State: `t` is a positive integer minus the total number of iterations executed, `n` is an input integer for each iteration, `k` is an input integer for each iteration, `a` is a list of integers updated with new input values split by spaces and converted to integers for each iteration, `x` is a list of integers obtained from the input using `map(int, input().split())` for each iteration.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will be 0 because it decreases by 1 with each iteration until it reaches 0. For each iteration, `n` and `k` will be the values entered by the user, `a` will be updated with the new list of integers entered by the user, and `x` will also be updated with the new list of integers entered by the user.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `k`, followed by two lists `a` and `x`. It then calls `func_1(a, x, k)` to check a certain condition. If the condition is met, it prints 'YES', otherwise it prints 'NO'. After processing all test cases, the function outputs the results for each case.

