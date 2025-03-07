#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 3 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 1 ≤ k ≤ 2 ⋅ 10^9. Additionally, there are two lists of integers a and x, where both lists have length n, and the elements of x are distinct integers satisfying -n ≤ x_i < x_{i+1} ≤ n with x_i ≠ 0.
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
        
    #State: Output State: The value of `t` will be decremented by 1 after each iteration of the loop. The value of `can_survive` will be either 'YES' or 'NO' based on the conditions inside the loop for each test case. After all iterations, `t` will be 0, and the `can_survive` values for each test case will be printed accordingly.
#Overall this is what the function does:The function processes multiple test cases (determined by `t`). For each test case, it reads integers `n` and `k`, followed by lists `a` and `x` of length `n`. It then sorts pairs of elements from `x` and `a` based on the absolute value of the elements from `x`. The function calculates whether, given `k` bullets per unit distance, the monsters represented by the pairs can be defeated without running out of bullets. If all monsters can be defeated for a test case, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function outputs 'YES' or 'NO' for each case based on the conditions checked.

