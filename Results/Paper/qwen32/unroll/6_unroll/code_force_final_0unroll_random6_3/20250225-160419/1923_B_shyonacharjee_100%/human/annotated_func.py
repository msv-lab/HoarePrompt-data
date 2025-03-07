#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4. For each test case, n and k are integers such that 1 <= n <= 3 * 10^5 and 1 <= k <= 2 * 10^9. a_i are integers such that 1 <= a_i <= 10^9 for all 1 <= i <= n. x_i are integers such that -n <= x_1 < x_2 < ... < x_n <= n and x_i != 0 for all 1 <= i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: For each test case, the output will be either 'YES' or 'NO' printed to the console, indicating whether it is possible to defeat all monsters with the given constraints. The variables `t`, `n`, `k`, `a`, `x`, `monsters`, `bullets_used`, and `can_survive` will not retain their values after the loop completes as they are local to each iteration. The state of `t` remains unchanged as it is the number of test cases to be processed.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each involving a set of monsters with specific health values and positions, and a given number of bullets. For each test case, it determines whether it is possible to defeat all monsters using the bullets, considering the distance each monster is from the starting point and a given parameter `k` that affects the number of bullets needed per unit distance. The function outputs 'YES' if all monsters can be defeated and 'NO' otherwise.

