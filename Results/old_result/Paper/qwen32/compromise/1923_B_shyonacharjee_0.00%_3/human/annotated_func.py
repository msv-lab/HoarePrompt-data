#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 1 ≤ k ≤ 2 · 10^9. a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9. x is a list of n integers where each element x_i satisfies -n ≤ x_i ≤ n, x_i ≠ 0, and the elements of x are in strictly increasing order. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `n` is the last input integer, `k` is the last input integer, `healths` is a list of integers obtained from the last input, `positions` is a list of integers obtained from the last input, `monsters` is a list of tuples sorted by the absolute value of the positions, `total_bullets_used` is the sum of the healths of all processed monsters for the last test case, `success` is True if all monsters were processed without exceeding available time for the last test case, otherwise False.
#Overall this is what the function does:The function `func_1` processes `t` test cases. For each test case, it checks if it is possible to defeat all `n` monsters using the given health values and positions within the constraints of the available time. It prints 'YES' if all monsters can be defeated without exceeding the time available for each monster, otherwise it prints 'NO'.

