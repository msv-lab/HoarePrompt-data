#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. Additionally, there are two lists of integers a and x, where a contains n integers such that 1 ≤ a_i ≤ 10^9, and x contains n integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
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
        
    #State: Output State: `success` is `False`, `i` is `n`, `position` is `monsters[n][0]`, `health` is `monsters[n][1]`, `distance` is `abs(monsters[n][0])`, `time_available` is `abs(monsters[n][0])`, `total_bullets_used` is the sum of all `health` values in the `monsters` list.
    #
    #Explanation: After the loop executes all its iterations, the loop condition `for i in range(n)` ensures that the loop runs exactly `n` times. Given that the loop sets `success` to `False` as soon as the condition `total_bullets_used + bullets_needed > time_available` is met, and this condition is met before the loop completes all iterations, `success` remains `False`. At the end of the loop, the variable `i` will be `n`, indicating that all `n` iterations have been completed. The last executed monster's details (`position`, `health`, `distance`, `time_available`) are those of the last monster in the `monsters` list, which is `monsters[n-1]`. However, since array indices start from 0, `monsters[n][0]` and `monsters[n][1]` refer to the position and health of the last monster respectively. The `total_bullets_used` is the cumulative sum of all `health` values of the monsters because the loop adds each `bullets_needed` (which is equal to `health`) to `total_bullets_used` without any reduction.
#Overall this is what the function does:The function processes a series of test cases, each involving a number of monsters with given positions and health points. For each test case, it calculates whether it is possible to defeat all monsters using a limited number of bullets, based on their positions and health. If it is possible to defeat all monsters within the given constraints, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but outputs the result for each test case.

