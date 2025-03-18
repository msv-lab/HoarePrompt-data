#State of the program right berfore the function call: a is a list of non-negative integers representing the health of n monsters, x is a list of integers representing the initial positions of the n monsters, and k is a non-negative integer representing the number of bullets you can fire per second. The length of a and x is n, and 1 <= n <= 3 * 10^5, 1 <= k <= 2 * 10^9. The values in x are sorted in ascending order and are non-zero, with -n <= x[i] < x[i+1] <= n for all i.
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
        
    #State: The value of `distance` is increased until either `pos` reaches the length of `sorted_indices` or the condition `abs(x[sorted_indices[pos]]) == distance` is met, resulting in a return statement. If the loop completes without returning, `distance` will be equal to the number of iterations plus one, and `pos` will be equal to the number of non-zero elements in `a[sorted_indices]`.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts three parameters: a list of non-negative integers `a`, representing the health of monsters, a list of integers `x`, representing the initial positions of the monsters, and a non-negative integer `k`, representing the number of bullets that can be fired per second. It returns True if it is possible to fire enough bullets to reduce the health of all monsters to zero within the given constraints.

#State of the program right berfore the function call: t is an integer representing the number of test cases; n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9; a is a list of n integers where each integer represents the health of a monster (1 ≤ a_i ≤ 10^9); x is a list of n integers where each integer represents the initial position of a monster (-n ≤ x_i < x_{i+1} ≤ n and x_i ≠ 0).
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: After executing the loop for all test cases, the output will consist of 'YES' or 'NO' for each test case based on the result of `func_1(a, x, k)`. Each 'YES' or 'NO' corresponds to whether the condition specified by `func_1` is met for the given inputs of n, k, a, and x for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of monsters (n), a threshold value (k), a list of monster healths (a), and a list of monster positions (x). It then calls another function `func_1(a, x, k)` to determine if a certain condition is met. Based on the result of `func_1`, it prints either 'YES' or 'NO' for each test case. The final state of the program consists of these 'YES' or 'NO' outputs for all test cases.

