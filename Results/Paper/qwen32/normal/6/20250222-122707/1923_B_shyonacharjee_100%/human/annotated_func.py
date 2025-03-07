#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and k is an integer such that 1 <= k <= 2 * 10^9. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9. x is a list of n integers where each element x_i satisfies -n <= x_i <= n, x_i are unique, and x is sorted in strictly increasing order. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is 0 such that 0 <= t <= 3 * 10^4; n and k are integers obtained from the second input line; a is a list of integers obtained from the third input line; x is a list of integers obtained from the fourth input line; monsters is a list of tuples sorted by the absolute value of the first element in each tuple; bullets_used is the sum of the healths of all processed monsters for the last test case; can_survive is False if the total bullets needed for any monster exceeded the allowed limit in the last test case, otherwise True.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it determines whether it is possible to defeat all monsters given their health and positions, and a limit on the number of bullets that can be used per unit distance. It prints 'YES' if all monsters can be defeated within the limit, otherwise 'NO'.

