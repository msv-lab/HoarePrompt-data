#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. Additionally, there are two lists of integers a and x, where both lists have length n, and a_i and x_i are integers such that 1 ≤ a_i ≤ 10^9 and -n ≤ x_1 < x_2 < ... < x_n ≤ n with x_i ≠ 0.
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
        
    #State: Output State: t test cases are processed, for each test case, we check if it's possible to defeat all monsters given the constraints on bullets and time. If it's possible for all test cases, the output is 'YES', otherwise it's 'NO'. The specific 'YES' or 'NO' for each test case depends on the input values of n, k, healths, and positions.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \), along with two lists of integers \( \text{positions} \) and \( \text{healths} \). For each test case, it determines whether it is possible to defeat all monsters using the given number of bullets within the available time. If it is possible to defeat all monsters in all test cases, the function outputs 'YES'; otherwise, it outputs 'NO'.

