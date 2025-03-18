#State of the program right berfore the function call: a is a list of positive integers representing the health of the monsters, x is a list of non-zero integers representing the initial positions of the monsters, and k is a positive integer representing the number of bullets you can fire each second. The lengths of a and x are equal, and each element in x is unique and sorted in ascending order.
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
        
    #State: `pos` is the length of `sorted_indices`, `distance` is the number of seconds it took to eliminate all monsters, and `a` is a list of non-positive integers representing the health of the monsters after all shots have been fired.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts three parameters: a list of positive integers `a` representing the health of the monsters, a list of non-zero integers `x` representing the initial positions of the monsters (unique and sorted in ascending order), and a positive integer `k` representing the number of bullets you can fire each second. The function attempts to eliminate all monsters by firing bullets at them in order of their proximity to the origin (0). If at any point a monster is at the same distance from the origin as the current `distance` (which increments each second), the function returns `False`. If all monsters are eliminated, the function returns `True`. After the function concludes, `a` is a list of non-positive integers representing the health of the monsters, and `distance` is the number of seconds it took to eliminate all monsters.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: The loop has executed `t` times, and for each iteration, the values of `n`, `k`, `a`, and `x` have been read from user input. The function `func_1(a, x, k)` has been called for each iteration, and the output of the loop will be a series of 'YES' or 'NO' messages, one for each iteration, based on the return value of `func_1`. The value of `t` remains unchanged.
#Overall this is what the function does:The function `func_2` reads an integer `t` from user input, where `1 <= t <= 30,000`. It then performs `t` iterations, each time reading two integers `n` and `k`, a list of integers `a`, and another list of integers `x` from user input. For each iteration, it calls the function `func_1(a, x, k)` and prints 'YES' if `func_1` returns `True`, or 'NO' if `func_1` returns `False`. After `t` iterations, the function completes, and the value of `t` remains unchanged.

