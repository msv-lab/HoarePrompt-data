#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4. For each test case, n and k are integers such that 1 <= n <= 3 * 10^5 and 1 <= k <= 2 * 10^9. a_1, a_2, ..., a_n are integers such that 1 <= a_i <= 10^9 for all 1 <= i <= n. x_1, x_2, ..., x_n are integers such that -n <= x_1 < x_2 < ... < x_n <= n and x_i != 0 for all 1 <= i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an input integer such that 1 <= `t` <= 3 * 10^4; `n` and `k` are integers read from the input; `a` is a list of integers read from the input; `x` is a list of integers read from the new input; `monsters` is a list of tuples sorted by the absolute value of the elements in `x`; `bullets_used` is the sum of all `health` values in `monsters` if `can_survive` is `True`, otherwise it is the sum of `health` values up to the point where `total_bullets_needed` exceeds `distance * k` for the last test case; `can_survive` is `True` if `total_bullets_needed` never exceeds `distance * k` for any tuple in the last test case, otherwise `False`. The loop has completed all `t` iterations and printed 'YES' or 'NO' for each test case.
#Overall this is what the function does:The function `func_1` processes `t` test cases, each consisting of two integers `n` and `k`, and two lists of integers `a` and `x`. For each test case, it determines whether it is possible to defeat all monsters, where each monster has a position `x[i]` and health `a[i]`, using bullets with a maximum range of `k` units. The function prints 'YES' if all monsters can be defeated without exceeding the bullet range for any monster, otherwise it prints 'NO'.

