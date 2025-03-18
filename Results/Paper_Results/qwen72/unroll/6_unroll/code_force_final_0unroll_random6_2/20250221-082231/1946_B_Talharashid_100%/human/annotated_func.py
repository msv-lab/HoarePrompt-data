#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers such that 1 ≤ n, k ≤ 2 · 10^5, and a is a list of n integers where -10^9 ≤ a_i ≤ 10^9.
def func():
    for i in range(int(input())):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        c = 0
        
        maxi = 0
        
        for ele in l:
            if ele < 0 and c <= abs(ele):
                maxi = max(c, maxi)
                c = 0
            else:
                c += ele
                maxi = max(c, maxi)
        
        maxi = max(c, maxi)
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: The variable `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `k` are integers such that 1 ≤ n, k ≤ 2 · 10^5, and `a` is a list of n integers where -10^9 ≤ a_i ≤ 10^9. The loop has executed `t` times, and for each iteration, the result of the expression `(2
#Overall this is what the function does:The function `func` reads an integer `t` and then, for `t` iterations, reads two integers `n` and `k`, followed by a list `l` of `n` integers. It calculates the maximum sum of a subsequence of `l` where the subsequence can reset when encountering a negative number. The function then computes and prints the result of the expression `(2

