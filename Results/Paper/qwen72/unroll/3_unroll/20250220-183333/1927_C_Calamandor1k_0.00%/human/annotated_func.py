#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n, m ≤ 2·10^5, k is an even integer such that 2 ≤ k ≤ 2·min(n, m), a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_j ≤ 10^6.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads new values for `n`, `m`, and `k`, and new lists `a` and `b`. After processing, it prints 'YES' if the number of elements in `a` and `b` that are less than or equal to `k` is at least `k // 2`, otherwise it prints 'NO'. The variables `n`, `m`, `k`, `a`, and `b` are reset for each iteration, and `t` is decremented by 1 after each iteration until the loop completes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, and two lists of integers `a` and `b` of lengths `n` and `m` respectively. It then checks if the number of elements in `a` and `b` that are less than or equal to `k` is at least `k // 2`. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After processing all `t` test cases, the function concludes.

