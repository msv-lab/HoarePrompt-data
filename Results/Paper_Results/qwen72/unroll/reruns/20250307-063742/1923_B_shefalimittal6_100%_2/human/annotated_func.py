#State of the program right berfore the function call: a is a list of positive integers representing the health of each monster, x is a list of distinct integers representing the initial positions of each monster, and k is a positive integer representing the number of bullets you can fire each second. The lengths of a and x are equal, and no element in x is zero.
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
        
    #State: `pos` is equal to the length of `sorted_indices`, `distance` is the number of seconds it took to eliminate all monsters, and all elements in `a` are 0.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` takes three parameters: a list `a` of positive integers representing the health of each monster, a list `x` of distinct integers representing the initial positions of each monster, and a positive integer `k` representing the number of bullets you can fire each second. The function processes the monsters in the order of their proximity to the origin (0), attempting to reduce their health to 0 by firing `k` bullets each second. If at any point a monster's position matches the current distance from the origin, the function returns `False`. If all monsters are eliminated, the function returns `True`. After the function concludes, all elements in `a` are 0, and the function has returned either `True` or `False` based on the conditions described.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: t remains an input integer such that 1 <= t <= 3 * 10^4, and the loop has executed t times, printing 'YES' or 'NO' for each iteration based on the result of func_1(a, x, k).
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, where `1 <= t <= 30,000`. It then iterates `t` times, each time reading two integers `n` and `k`, followed by two lists of integers `a` and `x`. For each iteration, it prints 'YES' if the function `func_1(a, x, k)` returns `True`, and 'NO' otherwise. After `t` iterations, the function completes, leaving `t` unchanged and having printed 'YES' or 'NO' for each test case.

