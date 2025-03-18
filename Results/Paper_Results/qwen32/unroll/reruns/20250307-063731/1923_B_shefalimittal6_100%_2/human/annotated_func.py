#State of the program right berfore the function call: a is a list of integers representing the health of monsters, x is a list of integers representing the initial positions of the monsters, and k is an integer representing the maximum number of bullets that can be fired per second. The length of a and x are equal, and x is sorted in ascending order with no duplicates and x_i != 0 for all i.
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
        
    #State: pos is equal to n, distance is the total number of iterations, rest is 0, a is a list of zeros, sorted_indices and x remain unchanged.
    return True
    #The program returns True
#Overall this is what the function does:The function checks if it is possible to defeat all monsters given their health and positions, using a maximum number of bullets per second. It returns `True` if all monsters can be defeated under these conditions, otherwise it returns `False`.

#State of the program right berfore the function call: a is a list of integers representing the health of each monster, x is a list of integers representing the initial positions of each monster such that -n <= x_i < x_2 < ... < x_n <= n and x_i != 0, and k is an integer representing the maximum number of bullets that can be fired per second.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `n` and `k` are the values read in the last iteration, `a` is the list of integers representing the health of each monster from the last iteration, and `x` is the list of integers representing the initial positions of each monster from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers representing the health of monsters, a list of integers representing their initial positions, and an integer representing the maximum number of bullets that can be fired per second. For each test case, it determines if it is possible to defeat all monsters and prints 'YES' if possible, otherwise 'NO'.

