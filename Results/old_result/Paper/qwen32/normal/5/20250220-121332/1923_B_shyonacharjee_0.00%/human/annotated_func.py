#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 · 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9. a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for each i. x is a list of n integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0 for each i. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0; `n` and `k` are the last input integers; `healths` is the last list of integers read from the input; `positions` is the last list of integers read from the input; `monsters` is a sorted list of tuples, where each tuple contains a position and a health value, sorted by the absolute value of the position; `total_bullets_used` is the sum of the health values of all monsters if `success` is `True`; `success` is `True` if `total_bullets_used` never exceeded `time_available` for any monster; otherwise, `success` is `False`.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it determines if it is possible to defeat all monsters within the constraints given. It accepts an integer `t` representing the number of test cases. For each test case, it takes two integers `n` and `k`, a list `a` of `n` integers representing the health of monsters, and a list `x` of `n` integers representing the positions of the monsters. The function outputs 'YES' if it is possible to defeat all monsters using the bullets within the time constraints, otherwise it outputs 'NO'.

