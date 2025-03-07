#State of the program right berfore the function call: a is a list of positive integers representing the health of each monster, x is a list of integers representing the initial positions of each monster relative to the player's position, and k is a positive integer representing the maximum number of bullets that can be fired per second. The lengths of a and x are equal, and for all elements x_i in x, x_i ≠ 0.
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
        
    #State: All monsters whose health could be reduced to 0 with the available bullets have been defeated. The `rest` variable is now 0, indicating that there are no more bullets left to fire. The `pos` variable is equal to the length of `sorted_indices`, indicating that all monsters have been processed. The `a` list contains the remaining health of each monster, where all elements are 0 if all monsters have been defeated. The `distance` variable is equal to the number of iterations the loop executed, which is the maximum distance at which the last monster was defeated. The `x`, `k`, `n`, and `sorted_indices` variables remain unchanged.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` takes three parameters: `a`, a list of positive integers representing the health of each monster; `x`, a list of integers representing the initial positions of each monster relative to the player's position; and `k`, a positive integer representing the maximum number of bullets that can be fired per second. The function processes the monsters in order of their proximity to the player, reducing their health with the available bullets until either all monsters are defeated or a monster reaches the player's position. If any monster reaches the player's position before being defeated, the function returns `False`. Otherwise, if all monsters are defeated before reaching the player, the function returns `True`. After the function concludes, the `a` list contains the remaining health of each monster, which will be all zeros if all monsters were defeated. The `x` and `k` parameters remain unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 3 * 10^4. n and k are positive integers where 1 ≤ n ≤ 3 * 10^5 and 1 ≤ k ≤ 2 * 10^9. a is a list of n positive integers where 1 ≤ a_i ≤ 10^9. x is a list of n distinct integers sorted in ascending order where -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `t` must be equal to the initial value of `t`, `_` is `t-1`, `n` and `k` are input integers, `a` is a list of integers input by the user, `x` is a list of integers input by the user.
#Overall this is what the function does:The function `func_2` reads multiple sets of inputs from the user, each set consisting of two integers `n` and `k`, a list of integers `a`, and a list of distinct integers `x`. For each set, it calls another function `func_1` with `a`, `x`, and `k` as arguments and prints 'YES' if `func_1` returns True, otherwise it prints 'NO'. The function processes `t` sets of inputs, where `t` is a positive integer provided initially. After processing all sets, the function terminates without returning any value.

