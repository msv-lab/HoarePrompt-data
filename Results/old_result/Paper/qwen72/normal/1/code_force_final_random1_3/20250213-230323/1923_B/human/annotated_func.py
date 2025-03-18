#State of the program right berfore the function call: a is a list of positive integers representing the health of each monster, x is a list of integers representing the initial positions of the monsters, and k is a positive integer representing the maximum number of bullets you can fire per second. The lengths of a and x are equal, and for each i, x[i] ≠ 0 and the x values are strictly increasing in absolute value.
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
        
    #State: After all iterations of the loop, the health of each monster in the list `a` will be reduced to 0 or lower, and the variable `pos` will be equal to the length of `sorted_indices`, indicating that all monsters have been defeated. The variable `distance` will be the final distance value reached during the loop's execution, which is the maximum distance any monster was from the origin when it was defeated. The variable `rest` will be 0, as all available bullets have been used or there are no more monsters to target. All other variables (`x`, `k`, `n`, `sorted_indices`) will retain their initial values.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` takes three parameters: `a` (a list of positive integers representing the health of each monster), `x` (a list of integers representing the initial positions of the monsters), and `k` (a positive integer representing the maximum number of bullets you can fire per second). It returns `True` if it is possible to defeat all the monsters by firing up to `k` bullets per second, and `False` otherwise. If the function returns `True`, all monsters' health in the list `a` will be reduced to 0 or lower, and the function will have processed all monsters in the order of their proximity to the origin. If the function returns `False`, it indicates that at least one monster could not be defeated under the given constraints. The lists `a` and `x`, and the integer `k` remain unchanged except for the modifications to the health values in `a`.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 3 · 10^4, representing the number of test cases. n and k are positive integers where 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9, representing the number of monsters and the maximum number of bullets you can fire per second, respectively. a is a list of n positive integers where 1 ≤ a_i ≤ 10^9, representing the health of each monster. x is a list of n distinct integers where -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0, representing the initial positions of the monsters relative to your character.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 3 · 10^4, `n` and `k` are updated to the values read from the input, `a` is a list of integers read from the input, `x` is a list of integers read from the input, `_` is `t-1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of monsters (`n`), the firing rate (`k`), the health of each monster (`a`), and their initial positions (`x`). For each test case, it determines whether it is possible to defeat all the monsters and prints 'YES' if it is possible, otherwise 'NO'. The function does not return any value; it only outputs the result for each test case. After the function concludes, the input variables `t`, `n`, `k`, `a`, and `x` are no longer relevant as they were used within the scope of the function.

