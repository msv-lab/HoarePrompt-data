#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 · 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9. a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 10^9 for each i. x_1, x_2, ..., x_n are integers such that -n ≤ x_1 < x_2 < x_3 < ... < x_n ≤ n and x_i ≠ 0 for each i. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: For each test case, it prints 'YES' if it is possible to defeat all monsters using the given constraints (bullets and time), otherwise it prints 'NO'. The variables `t`, `n`, `k`, `healths`, `positions`, `monsters`, `total_bullets_used`, and `success` are in their final states after processing all test cases, but since they are loop variables, their specific values are not preserved outside the loop. The initial state of `t` remains unchanged as it is the number of test cases, and the input values for each test case are processed independently.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of monsters `n`, a maximum number of bullets `k`, a list of monster healths, and a list of their positions. For each test case, it determines whether it is possible to defeat all monsters using the bullets within the time constraints based on their positions and healths, and prints 'YES' if possible, otherwise 'NO'.

