#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. Additionally, there are two lists of integers a and x, where both lists have length n, and the elements of x are unique, sorted in strictly increasing order, and satisfy -n ≤ x_i ≤ n with x_i ≠ 0 for all i.
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
        
    #State: Output State: The output state consists of 'YES' or 'NO' printed for each test case based on whether it's possible to defeat all monsters given the constraints. For each test case, 'YES' is printed if the total number of bullets used does not exceed the available time for all monsters, otherwise 'NO' is printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \), and two lists of integers \( \text{positions} \) and \( \text{healths} \). For each test case, it determines whether it is possible to defeat all monsters using the given number of bullets within the allowed time. If it is possible, it prints 'YES'; otherwise, it prints 'NO'. The function reads inputs from standard input and outputs results to standard output.

