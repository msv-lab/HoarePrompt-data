#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 · 10^4, representing the number of test cases. Each test case in test_cases is a tuple containing (n, k, a, x) where n is an integer such that 1 ≤ n ≤ 3 · 10^5, k is an integer such that 1 ≤ k ≤ 2 · 10^9, a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and x is a list of n integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        healths = list(map(int, input().split()))
        
        positions = list(map(int, input().split()))
        
        monsters = sorted(zip(positions, healths), key=lambda x: abs(x[0]))
        
        total_bullets_used = 0
        
        success = True
        
        for i in range(n):
            position, health = monsters[i]
            distance = abs(position)
            time_available = distance
            bullets_needed = health
            if total_bullets_used + bullets_needed > time_available:
                success = False
                break
            total_bullets_used += bullets_needed
        
        print('YES' if success else 'NO')
        
    #State: The loop iterates through each test case, and for each test case, it determines whether it is possible to defeat all monsters by shooting them before they reach the player. The final state of the loop is that `t` test cases have been processed, and for each test case, the output is either 'YES' if all monsters can be defeated, or 'NO' if at least one monster cannot be defeated. The variables `n`, `k`, `healths`, `positions`, `monsters`, `total_bullets_used`, and `success` are reset for each test case, and the loop prints the result for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n`, an integer `k`, a list of `n` integers `a` (representing the healths of monsters), and a list of `n` distinct integers `x` (representing the positions of monsters). For each test case, it determines whether it is possible to defeat all monsters by shooting them before they reach the player. The function prints 'YES' if all monsters can be defeated, and 'NO' if at least one monster cannot be defeated. The function processes `t` test cases, where `t` is an integer such that 1 ≤ t ≤ 3 · 10^4, and the final state of the program is that all test cases have been processed and the results have been printed. The function does not return any value.

