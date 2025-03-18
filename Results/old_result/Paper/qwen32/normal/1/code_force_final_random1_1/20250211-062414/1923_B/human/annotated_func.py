#State of the program right berfore the function call: a is a list of integers representing the health of monsters, x is a list of integers representing the initial positions of monsters such that -n <= x[i] < x[i+1] <= n and x[i] != 0 for all i, and k is an integer representing the maximum number of bullets that can be fired per second.
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
        
    #State: `a` is a list of integers representing the remaining health of monsters after all possible shots have been fired; `x`, `k`, `n`, `sorted_indices` remain unchanged; `pos` is `len(sorted_indices)`; `distance` is the smallest integer such that all monsters within that distance have been fully targeted or there are no more monsters to target; `rest` is 0.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` determines whether it is possible to completely eliminate all monsters by firing bullets at them from a central position, given constraints on their initial positions and health, and a limit on the number of bullets that can be fired per second. It returns `False` if any monster cannot be eliminated under these conditions, and `True` otherwise.

#State of the program right berfore the function call: a is a list of integers representing the health of n monsters, x is a list of integers representing the initial positions of n monsters such that -n <= x_1 < x_2 < ... < x_n <= n and x_i != 0, and k is an integer representing the maximum number of bullets that can be fired per second.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `a`, `x`, `n`, `k`, and `t` are the last set of values read from the input, with `t` being 0. The loop has finished executing all its iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of monsters, their health values, their positions, and the maximum number of bullets that can be fired per second. For each test case, it determines whether it is possible to defeat all monsters under the given constraints and prints 'YES' if possible, otherwise 'NO'.

