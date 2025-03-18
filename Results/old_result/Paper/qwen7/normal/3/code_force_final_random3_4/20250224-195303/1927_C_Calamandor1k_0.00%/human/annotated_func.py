#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^5; k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m); a is a list of n integers such that 1 ≤ a_i ≤ 10^6; b is a list of m integers such that 1 ≤ b_j ≤ 10^6; the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        len_a, len_b = len(a), len(b)
        
        count_a, count_b = 0, 0
        
        d = k // 2
        
        for i in range(max(len_a, len_b)):
            if len_a > i + 1:
                if a[i] <= k:
                    count_a += 1
            if len_b > i + 1:
                if b[i] <= k:
                    count_b += 1
        
        print('YES' if count_a >= d and count_b >= d else 'NO')
        
    #State: Output State: After all iterations of the loop have finished, `d` is `k // 2`, `a` is a list of integers from the final input split, `n`, `m`, and `k` are integers from the final input split, `b` is updated to a list of integers from the final input split, `len_a` is the length of the final list `a`, `len_b` is the length of the final list `b`, `count_a` is the total number of elements in the final `a` that are less than or equal to `k`, `count_b` is the total number of elements in the final `b` that are less than or equal to `k`, `i` is equal to `max(len_a, len_b)`, and `t` is 1.
    #
    #In this final state, the loop has completed all its iterations based on the initial value of `t`. The values of `a` and `b` are updated to the last inputs provided, and the counts `count_a` and `count_b` reflect the number of elements in these lists that are less than or equal to `k`. The variable `i` is set to the maximum length between the final lists `a` and `b`, indicating the number of iterations the loop has completed. The variable `t` is reduced to 1 since all iterations have been executed, and the other variables retain their final states as described.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers \( t \), \( n \), \( m \), and \( k \), along with two lists \( a \) and \( b \). For each test case, it checks if the number of elements in lists \( a \) and \( b \) that are less than or equal to \( k/2 \) meet certain criteria. If both lists meet the criteria, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function outputs the results for each case.

