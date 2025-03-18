#State of the program right berfore the function call: a is a list of non-negative integers representing the health of n monsters, x is a list of n integers representing the initial positions of the monsters, and k is a non-negative integer representing the number of bullets you can fire per second.
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
        
    #State: The output state is such that the variable `distance` is incremented for each iteration of the outer while loop until either `rest` (the remaining bullets) becomes zero or `pos` reaches the length of `sorted_indices`. For each inner while loop, the script fires up to `delta` bullets at the monster at index `sorted_indices[pos]`, reducing its health (`a[sorted_indices[pos]]`) accordingly. If a monster's health is reduced to zero, its index is skipped in the next iteration. The final value of `distance` will be the number of times the outer loop iterates before either `rest` runs out or all monsters are defeated.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts three parameters: a list of non-negative integers `a` representing the health of monsters, a list of integers `x` representing the initial positions of the monsters, and a non-negative integer `k` representing the number of bullets that can be fired per second. It returns True if it is possible to defeat all monsters using the given number of bullets per second, based on their positions and health. The function sorts the monsters by their distance from the origin, then attempts to fire bullets at them in order, reducing their health. If all monsters' health can be reduced to zero using the available bullets, the function returns True; otherwise, it returns False.

#State of the program right berfore the function call: t is an integer representing the number of test cases; n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9; a is a list of n integers where 1 ≤ a_i ≤ 10^9; x is a list of n integers where -n ≤ x_i < x_{i+1} ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: t is the number of test cases executed, n and k are the last values read from the input for the current test case, a is the last list of integers read for the current test case, x is the last list of integers read for the current test case, the output consists of 'YES' or 'NO' printed for each test case based on the evaluation of func_1(a, x, k).
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the values of \( n \), \( k \), a list of integers \( a \), and another list of integers \( x \). It then calls `func_1(a, x, k)` to evaluate certain conditions. Based on the result of `func_1`, it prints either 'YES' or 'NO' for each test case. After processing all test cases, the function does not return any value but outputs the results of each test case.

