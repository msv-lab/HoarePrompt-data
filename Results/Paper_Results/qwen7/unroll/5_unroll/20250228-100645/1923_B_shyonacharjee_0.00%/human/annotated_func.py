#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. The list a contains n integers such that 1 ≤ a_i ≤ 10^9, and the list x contains n integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
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
        
    #State: Output State: t test cases are processed, for each test case, the program prints 'YES' if the player can defeat all monsters with the given bullets, otherwise it prints 'NO'. The player's success depends on whether they have enough bullets to defeat each monster within the available time based on the monster's position and health.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers t, n, k, a (a list of n integers), and x (a list of n integers). It then determines whether a player can defeat all monsters using the given number of bullets, based on the monsters' positions and health. If the player can defeat all monsters, it prints 'YES'; otherwise, it prints 'NO'.

