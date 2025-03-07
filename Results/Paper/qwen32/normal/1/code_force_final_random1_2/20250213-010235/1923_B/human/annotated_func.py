#State of the program right berfore the function call: a is a list of integers representing the health of monsters, x is a list of integers representing the initial positions of the monsters, and k is an integer representing the maximum number of bullets that can be fired per second. The length of a and x is the same and represents the number of monsters, n.
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
        
    #State: `a` is a list of zeros, `x` is unchanged, `k` is unchanged, `n` is unchanged, `sorted_indices` is unchanged, `distance` is the maximum distance any monster was from the starting point plus one, `pos` is the length of `sorted_indices`.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` determines whether it is possible to defeat all monsters by firing bullets such that no two monsters are at the same distance from the starting point when they are defeated. It accepts a list `a` of integers representing the health of monsters, a list `x` of integers representing their initial positions, and an integer `k` representing the maximum number of bullets that can be fired per second. The function modifies the list `a` to set the health of defeated monsters to zero and returns `False` if any two monsters are at the same distance from the starting point when they are defeated, otherwise it returns `True`.

#State of the program right berfore the function call: a is a list of n integers representing the health of each monster, x is a list of n integers representing the initial positions of each monster such that -n <= x_1 < x_2 < ... < x_n <= n and x_i != 0, and k is an integer representing the maximum number of bullets that can be fired per second.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: t is 0, n, k, a, and x are the values from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of a list of integers representing the health of each monster, a list of integers representing the initial positions of each monster, and an integer representing the maximum number of bullets that can be fired per second. For each test case, it determines whether it is possible to defeat all monsters under the given constraints and prints 'YES' if possible, otherwise 'NO'.

