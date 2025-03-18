#State of the program right berfore the function call: a is a list of integers representing the health of n monsters, x is a list of integers representing the initial positions of n monsters such that -n <= x[i] < x[i+1] <= n and x[i] != 0 for all i, k is an integer representing the maximum number of bullets that can be fired in one second.
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
        
    #State: `pos` is equal to the length of `sorted_indices`, and `distance` is incremented to a value greater than or equal to the maximum absolute position in `x`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` determines whether it is possible to eliminate all monsters by firing bullets such that no two monsters are at the same distance from the origin at the same time, given their initial health and positions, and the maximum number of bullets that can be fired in one second. It returns `True` if all monsters can be eliminated under these conditions, otherwise it returns `False`.

#State of the program right berfore the function call: a is a list of integers representing the health of n monsters, x is a list of integers representing the positions of n monsters such that -n <= x[0] < x[1] < ... < x[n-1] <= n and x[i] != 0 for all i, and k is an integer representing the maximum number of bullets that can be fired in one second.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `a` is a list of integers representing the health of n monsters, `x` is a list of integers representing the positions of n monsters such that -n <= x[0] < x[1] < ... < x[n-1] <= n and x[i] != 0 for all i, and `k` is an integer representing the maximum number of bullets that can be fired in one second; `t` is an input integer.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers representing the health of monsters, a list of integers representing their positions, and an integer representing the maximum number of bullets that can be fired in one second. For each test case, it determines whether it is possible to kill all monsters within the given constraints and prints 'YES' if possible, otherwise 'NO'.

