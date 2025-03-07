#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. The second line of each test case contains n integers a_1, a_2, \dots, a_n where 1 ≤ a_i ≤ 10^9. The third line of each test case contains n integers x_1, x_2, \dots, x_n where -n ≤ x_1 < x_2 < x_3 < \dots < x_n ≤ n and x_i ≠ 0. Additionally, the sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: After the loop executes all iterations, `i` is `n-1`, `success` is `False`, `total_bullets_used` is the sum of the `health` values of all monsters, `bullets_needed` is the last `health` value, `position` is `monsters[n-1][0]`, `health` is `monsters[n-1][1]`, `distance` is `abs(position)`, and `time_available` is `distance`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, k, a sequence of health values, and a sequence of positions. For each test case, it calculates whether it's possible to defeat all monsters within the given constraints. If it's possible, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

