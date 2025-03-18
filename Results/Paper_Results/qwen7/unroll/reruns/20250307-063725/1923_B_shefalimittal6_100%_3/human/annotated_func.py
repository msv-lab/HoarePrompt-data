#State of the program right berfore the function call: a is a list of non-negative integers representing the health of the monsters, x is a list of integers representing the initial positions of the monsters, and k is a non-negative integer representing the number of bullets you can fire per second. The length of a and x is n, and 1 <= n <= 3 * 10^5; 1 <= k <= 2 * 10^9.
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
        
    #State: The output state will be such that the list `a` (health of the monsters) will be modified according to the firing of bullets, and the variable `distance` will be incremented for each iteration of the outer while loop until the condition `pos == len(sorted_indices)` is met. If at any point during the execution, the absolute value of the position `x[sorted_indices[pos]]` equals `distance`, the function will return `False`. Otherwise, the function will continue to decrement the health of the monsters by the number of bullets fired (`k`) until their health reaches zero, then move to the next monster. The variable `pos` will keep track of which monster is being targeted, and `rest` will keep track of the remaining bullets in the current iteration of the inner while loop.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a list of non-negative integers representing the health of monsters (`a`), a list of integers representing the initial positions of the monsters (`x`), and a non-negative integer representing the number of bullets that can be fired per second (`k`). It returns `True` if it's possible to fire enough bullets to reduce the health of all monsters to zero, given the constraints. If at any point the absolute position of a monster equals the current distance, the function returns `False`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. x is a list of n integers where -n ≤ x_i < x_{i+1} ≤ n and x_i ≠ 0 for all 1 ≤ i ≤ n.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4, and now t is set to the same input integer. The value of `n`, `k`, `a`, and `x` are determined by each iteration of the loop, and the output consists of 'YES' or 'NO' based on the evaluation of `func_1(a, x, k)` for each test case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads values for \( n \), \( k \), a list of integers \( a \), and another list of integers \( x \). It then calls `func_1(a, x, k)` to evaluate certain conditions and prints 'YES' if the condition is met, otherwise 'NO'. After processing all test cases, the function does not return any value but outputs the results for each case.

