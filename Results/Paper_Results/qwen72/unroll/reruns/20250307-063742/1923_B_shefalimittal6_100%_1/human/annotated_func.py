#State of the program right berfore the function call: a is a list of integers representing the health of each monster, x is a list of integers representing the initial positions of each monster, and k is a positive integer representing the number of bullets you can fire each second. The lengths of a and x are equal, and for each i, 1 <= a[i] <= 10^9 and -n <= x[i] < x[i+1] <= n with x[i] != 0.
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
        
    #State: `pos` is equal to the length of `sorted_indices`, `distance` is the number of iterations the loop has run, and all elements in `a` corresponding to indices in `sorted_indices` are reduced by the total number of bullets fired, with some possibly reduced to 0.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts three parameters: a list of integers `a` representing the health of each monster, a list of integers `x` representing the initial positions of each monster, and a positive integer `k` representing the number of bullets you can fire each second. The function attempts to reduce the health of each monster to zero by firing bullets in a specific order based on the distance of the monsters from the origin. If at any point a monster's position matches the current distance, the function returns `False`. If all monsters' health can be reduced to zero without any position matching the current distance, the function returns `True`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: The value of `t` remains unchanged, and the loop has executed `t` times. For each iteration, `n`, `k`, `a`, and `x` are updated based on user input, and the result of `func_1(a, x, k)` is printed as 'YES' or 'NO'. After the loop, `n`, `k`, `a`, and `x` will hold the values from the last iteration.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, where `1 <= t <= 3 * 10^4`. For each of the `t` test cases, it reads two integers `n` and `k`, followed by two lists of integers `a` and `x` from the user input. It then calls `func_1(a, x, k)` and prints 'YES' if the result is `True`, or 'NO' if the result is `False`. After processing all `t` test cases, the function completes, and the value of `t` remains unchanged. The final state of the program is that `t` test cases have been processed, and the results for each test case have been printed.

