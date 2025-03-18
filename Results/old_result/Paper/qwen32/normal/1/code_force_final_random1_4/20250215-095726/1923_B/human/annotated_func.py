#State of the program right berfore the function call: a is a list of integers representing the health of n monsters, x is a list of integers representing the initial positions of n monsters such that -n <= x[i] < x[i+1] <= n and x[i] != 0 for all i, and k is an integer representing the maximum number of bullets that can be fired per second.
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
        
    #State: a = [0, 0, 0], x = [-2, 1, -3], k = 10, n = 3, sorted_indices = [1, 0, 2], distance = 2, pos = 3, rest = 8.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` determines whether it is possible to defeat all monsters by firing bullets at them based on their health and positions, given a limit on the number of bullets that can be fired per second. It returns `False` if any monster cannot be defeated before reaching a position where its distance from the origin matches the number of steps taken, otherwise, it returns `True`.

#State of the program right berfore the function call: a is a list of integers representing the health of each monster, x is a list of integers representing the initial positions of each monster, and k is an integer representing the maximum number of bullets that can be fired per second. The lengths of a and x are equal and represent the number of monsters, n.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `a` is the list of integers read from the input during the last iteration, `x` is the list of integers read from the input during the last iteration, `k` is the integer read from the input during the last iteration, `n` is the integer read from the input during the first iteration, and `t` is 0.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers representing the health of monsters, a list of integers representing their initial positions, and an integer representing the maximum number of bullets that can be fired per second. For each test case, it determines whether it is possible to defeat all the monsters under the given constraints and prints 'YES' if possible, otherwise 'NO'.

