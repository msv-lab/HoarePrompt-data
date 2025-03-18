#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5, k is an even integer such that 2 <= k <= 2 * min(n, m). a is a list of n integers where each integer is between 1 and 10^6. b is a list of m integers where each integer is between 1 and 10^6. The sum of n and m over all test cases does not exceed 4 * 10^5.
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
        
    #State: `t` is an integer such that `t` == 0; `n`, `m`, and `k` are integers read from the input in the last iteration; `a` is a list of integers read from the input in the last iteration; `b` is a list of integers read from the input in the last iteration; `len_a` is the length of the list `a` from the last iteration; `len_b` is the length of the list `b` from the last iteration; `d` is `k // 2` from the last iteration; `count_a` is the number of elements in `a` that are less than or equal to `k` from the last iteration; `count_b` is the number of elements in `b` that are less than or equal to `k` from the last iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if at least half of the elements in each of two lists are less than or equal to a given even integer `k`. It outputs 'YES' if both conditions are met for a test case, otherwise it outputs 'NO'.

