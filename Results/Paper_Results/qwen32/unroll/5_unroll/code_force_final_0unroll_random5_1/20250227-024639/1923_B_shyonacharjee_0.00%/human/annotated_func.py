#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 1 ≤ k ≤ 2 · 10^9. a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9. x is a list of n integers where each element x_i satisfies -n ≤ x_i < x_{i+1} ≤ n and x_i ≠ 0 for all i. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 3 · 10^4; `n` is an integer such that 1 ≤ n ≤ 3 · 10^5, and `k` is an integer such that 1 ≤ k ≤ 2 · 10^9. `a` is a list of `n` integers where each element `a_i` satisfies 1 ≤ `a_i` ≤ 10^9. `x` is a list of `n` integers where each element `x_i` satisfies -`n` ≤ `x_i` < `x_{i+1}` ≤ `n` and `x_i` ≠ 0 for all `i`. The sum of `n` over all test cases does not exceed 3 · 10^5.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a number of monsters `n`, a maximum bullet capacity `k`, a list of monster health values `a`, and a list of their positions `x`. For each test case, it determines if it is possible to defeat all monsters using bullets, where the number of bullets required equals the monster's health and must be used within the absolute value of the monster's position. It prints 'YES' if all monsters can be defeated under these conditions, otherwise 'NO'.

