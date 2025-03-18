#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are positive integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers such that 1 <= p_i <= n for all 1 <= i <= n. a is a list of n integers such that 1 <= a_i <= 10^9. The sum of values of n over all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    for i in range(t):
        n, k, b, s = list(map(int, input().split()))
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        b -= 1
        
        s -= 1
        
        sp = a[s]
        
        bp = a[b]
        
        bm = a[b] * k
        
        sm = a[s] * k
        
        for i in range(n):
            k -= 1
            if k == 0:
                break
            b = p[b] - 1
            s = p[s] - 1
            bm = max(bm, a[b] * k + bp)
            sm = max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: For each of the t test cases, the program will output either 'Bodya', 'Sasha', or 'Draw' based on the comparison between the maximum possible scores of Bodya and Sasha after k moves. The values of t, n, k, P_B, P_S, p, and a remain unchanged after the loop executes.
#Overall this is what the function does:The function processes multiple test cases, each involving a set of parameters and lists, to determine the winner between Bodya and Sasha based on their maximum possible scores after a specified number of moves. For each test case, it outputs either 'Bodya', 'Sasha', or 'Draw' depending on the comparison of their scores. The input parameters and lists remain unchanged after processing each test case.

