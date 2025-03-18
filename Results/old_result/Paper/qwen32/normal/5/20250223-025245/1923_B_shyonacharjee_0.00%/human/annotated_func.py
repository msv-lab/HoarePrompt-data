#State of the program right berfore the function call: t is an integer such that 1 <= t <= 3 * 10^4. For each test case, n and k are integers such that 1 <= n <= 3 * 10^5 and 1 <= k <= 2 * 10^9. a is a list of n integers such that 1 <= a_i <= 10^9 for each i. x is a list of n integers such that -n <= x_1 < x_2 < ... < x_n <= n and x_i != 0 for each i. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is the total number of test cases processed; `n` and `k` are the integers from the last test case's input; `healths` is the list of integers from the last test case's input; `positions` is the list of integers from the last test case's input; `monsters` is a list of tuples (position, health) sorted by the absolute value of the position for the last test case; `total_bullets_used` is the sum of the health values of all monsters in the last test case if `success` is True; `position` and `health` are from the last monster in `monsters` of the last test case; `distance` and `time_available` are the absolute value of the last position in the last test case; `bullets_needed` is the health of the last monster in the last test case; `success` is True if the total bullets used never exceeded the time available for each monster in the last test case, otherwise False.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it determines if it is possible to defeat all monsters within the constraints given their health and positions. It outputs 'YES' if all monsters can be defeated, otherwise 'NO'.

