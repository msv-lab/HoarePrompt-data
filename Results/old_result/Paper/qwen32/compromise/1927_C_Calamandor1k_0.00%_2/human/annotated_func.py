#State of the program right berfore the function call: For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5, k is an even integer such that 2 <= k <= 2 * min(n, m), a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, and b is a list of m integers where each integer b_j satisfies 1 <= b_j <= 10^6. The sum of all n and m across all test cases does not exceed 4 * 10^5.
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
        
    #State: `t` is 0 such that `t` >= 0; `n`, `m`, and `k` are integers read from input; `a` is a list of integers read from input; `b` is a list of integers read from input; `len_a` is the length of the list `a`; `len_b` is the length of the list `b`; `d` is `k // 2`; `count_a` is the number of elements in `a` that are less than or equal to `k`; `count_b` is the number of elements in `b` that are less than or equal to `k`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `n` and `m`, an even integer `k`, a list `a` of `n` integers, and a list `b` of `m` integers. For each test case, it checks if at least half of the elements in both lists `a` and `b` are less than or equal to `k`. It prints 'YES' if both conditions are met, otherwise it prints 'NO'.

