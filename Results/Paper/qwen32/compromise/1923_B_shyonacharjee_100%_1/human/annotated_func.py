#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and k is an integer such that 1 <= k <= 2 * 10^9. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. x is a list of n integers where each integer x_i satisfies -n <= x_i <= n, x_i != 0, and the list x is strictly increasing (i.e., x_1 < x_2 < ... < x_n). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t remains unchanged, n and k are integers read from the input, a is a list of integers read from the input, x is a list of integers read from the input, monsters is a sorted list of tuples based on the absolute value of the first element of each tuple, bullets_used is the sum of the health values of all processed monsters for the current test case, can_survive is False if any total_bullets_needed exceeds distance * k for any monster in the current test case, otherwise True.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an integer `n`, an integer `k`, a list `a` of integers representing monster health, and a list `x` of integers representing monster positions. For each test case, it determines if it is possible to defeat all monsters using bullets, where the number of bullets needed for each monster is equal to its health, and the total number of bullets used cannot exceed `k` times the distance to the monster. The function outputs 'YES' if all monsters can be defeated under these conditions, otherwise 'NO'.

