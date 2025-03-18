#State of the program right berfore the function call: a is a list of integers representing the health of the monsters, x is a list of integers representing the initial positions of the monsters, and k is an integer representing the maximum number of bullets that can be fired in one second. The lengths of a and x are equal, and x is sorted in strictly increasing order with no element equal to 0.
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
        
    #State: `a` is modified with some values potentially reduced to 0; `x`, `k`, `n`, `sorted_indices` remain unchanged; `distance` is equal to the length of `sorted_indices`; `pos` is equal to the length of `sorted_indices`.
    return True
    #The program returns True
#Overall this is what the function does:The function determines if it is possible to shoot all monsters with a given maximum number of bullets per second, without shooting any monster at the same distance from the starting point in the same second. It modifies the list `a` to reflect the remaining health of the monsters after the simulated shooting. The function returns `True` if all monsters can be shot under these conditions, and `False` otherwise.

#State of the program right berfore the function call: a is a list of integers representing the health of each monster, x is a list of integers representing the initial positions of each monster such that -n <= x[i] < x[i+1] <= n for all i, and k is an integer representing the maximum number of bullets that can be fired in one second.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `a` is the list of integers representing the health of each monster from the last iteration, `x` is the list of integers representing the initial positions of each monster from the last iteration, and `k` is the integer representing the maximum number of bullets that can be fired in one second from the last iteration. The variable `t` remains unchanged.
#Overall this is what the function does:The function `func_2` reads multiple test cases from the input. For each test case, it reads the number of monsters `n` and the maximum number of bullets `k` that can be fired in one second. It then reads two lists: `a`, which contains the health of each monster, and `x`, which contains the initial positions of each monster. The function determines if it is possible to defeat all the monsters given the constraints and prints 'YES' if it is possible, otherwise 'NO'.

