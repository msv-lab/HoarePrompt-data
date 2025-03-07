#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4. For each test case, n and k are integers such that 1 <= n <= 3 * 10^5 and 1 <= k <= 2 * 10^9. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9. x is a list of n integers where each element x_i satisfies -n <= x_i <= n, x_i != 0, and the elements are strictly increasing (x_1 < x_2 < ... < x_n). The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        monsters = sorted(zip(x, a), key=lambda p: abs(p[0]))
        
        bullets_used = 0
        
        can_survive = True
        
        for pos, health in monsters:
            distance = abs(pos)
            total_bullets_needed = bullets_used + health
            if total_bullets_needed > distance * k:
                can_survive = False
                break
            bullets_used += health
        
        print('YES' if can_survive else 'NO')
        
    #State: For each test case, the program will output either 'YES' or 'NO' indicating whether it is possible to defeat all monsters with the given constraints. The variables `t`, `n`, `k`, `a`, and `x` will retain their input values as they are not modified within the loop body. The variable `bullets_used` will be reset to 0 at the start of each test case iteration, and `can_survive` will be set to True. The list `monsters` is a sorted version of the zipped `x` and `a` lists based on the absolute value of `x`, and it will be recalculated for each test case.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a number of monsters `n`, a bullet limit `k`, a list of monster health values `a`, and a list of monster positions `x`. For each test case, it determines whether it is possible to defeat all monsters using the given constraints and outputs 'YES' if possible, otherwise 'NO'.

