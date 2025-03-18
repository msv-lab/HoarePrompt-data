#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. Additionally, there are two lists of integers: a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, and a list of n integers x_1, x_2, ..., x_n where -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4, and for each i from 1 to t, the output is either 'YES' or 'NO' based on whether the player can survive all the monster attacks given the constraints.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and k, a list of n integers representing monster health (a), and a list of n integers representing positions (x). It sorts the monsters based on their positions and checks if the player can survive all monster attacks within the given constraints. If the player can survive all attacks for a test case, it prints 'YES'; otherwise, it prints 'NO'. The function outputs 'YES' or 'NO' for each test case.

