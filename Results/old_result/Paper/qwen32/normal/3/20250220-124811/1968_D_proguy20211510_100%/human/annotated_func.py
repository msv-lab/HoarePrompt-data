#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are positive integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each integer is between 1 and n inclusive. a is a list of n integers where each integer is between 1 and 10^9 inclusive. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    YES, NO = 'YES', 'NO'
    MOD = 10 ** 9 + 7
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(int(input())):
        n, k, pb, ps = input().split()
        
        n, k, pb, ps = int(n), int(k), int(pb), int(ps)
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        pathb, paths = [], []
        
        vis = [0] * n
        
        vis[pb - 1] = 1
        
        while True:
            pathb.append(a[pb - 1])
            pb = p[pb - 1]
            if vis[pb - 1] == 1:
                break
        
        vis = [0] * n
        
        vis[ps - 1] = 1
        
        while True:
            paths.append(a[ps - 1])
            ps = p[ps - 1]
            if vis[ps - 1] == 1:
                break
        
        resb, ress = 0, 0
        
        preb, pres = 0, 0
        
        for i in range(len(pathb)):
            if k < i + 1:
                break
            curr = preb + pathb[i] * (k - i)
            preb += pathb[i]
            resb = max(resb, curr)
        
        for i in range(len(paths)):
            if k < i + 1:
                break
            curr = pres + paths[i] * (k - i)
            pres += paths[i]
            ress = max(ress, curr)
        
        if resb > ress:
            print('Bodya')
        elif ress > resb:
            print('Sasha')
        else:
            print('Draw')
        
    #State: The loop has processed all `t` test cases, and for each test case, it has determined whether 'Bodya', 'Sasha', or a 'Draw' occurs based on the maximum possible score each can achieve within `k` steps.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `P_B`, `P_S`, and two lists `p` and `a`. For each test case, it determines the maximum possible score that two players, Bodya and Sasha, can achieve within `k` steps based on the values in `p` and `a`, starting from positions `P_B` and `P_S` respectively. It then prints 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if their scores are equal.

