#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 · 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9. a_i is an integer such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. x_i is an integer such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0 for all 1 ≤ i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 3 · 10^4; n and k are integers such that 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9; a_i is an integer such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n; x_i is an integer such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0 for all 1 ≤ i ≤ n; The sum of n over all test cases does not exceed 3 · 10^5. After executing the loop, for each test case, the program will print 'YES' if it is possible to defeat all monsters with the available bullets within the time constraints, otherwise it will print 'NO'. The values of t, n, k, a_i, and x_i remain unchanged from the initial state.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a number of monsters `n`, a value `k` (not used in the function), a list of monsters' health values `a_i`, and a list of their positions `x_i`. For each test case, it determines if it is possible to defeat all monsters using the available bullets within the time constraints, where the time constraint for each monster is the absolute value of its position. It prints 'YES' if all monsters can be defeated, otherwise it prints 'NO'. The function does not modify the input values.

