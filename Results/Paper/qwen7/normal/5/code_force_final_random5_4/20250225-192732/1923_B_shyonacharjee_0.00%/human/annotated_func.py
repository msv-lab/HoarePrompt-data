#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 10^9. x_1, x_2, ..., x_n are integers such that -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `success` is False, `monsters` remains a list of tuples sorted by the absolute value of the positions, `i` is `n`, `position` is undefined, `health` is undefined, `distance` is undefined, `time_available` is undefined, `bullets_needed` is undefined, `total_bullets_used` is the sum of `bullets_needed` for all iterations.
    #
    #Explanation: After the loop completes all its iterations, the loop condition `i < n` will no longer be satisfied since `i` will be incremented up to `n-1` and then to `n`. The variable `success` remains `False` because it was set to `False` during one of the iterations and never changed afterward. The `monsters` list remains unchanged as no modifications were made to it within the loop. The `i` variable is set to `n` indicating that all elements in the `monsters` list have been processed. All other variables that were updated inside the loop are no longer relevant since the loop has ended, and thus they are undefined.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, k, a list of integers healths, and a list of integers positions. For each test case, it checks whether it is possible to defeat all monsters using the available bullets within the given time. If it is possible, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

