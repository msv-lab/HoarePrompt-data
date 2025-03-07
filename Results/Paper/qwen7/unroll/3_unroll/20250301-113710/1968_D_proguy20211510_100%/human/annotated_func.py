#State of the program right berfore the function call: t is a positive integer, and for each test case, n, k, P_B, P_S are positive integers such that 1 \leq P_B, P_S \leq n \leq 2 \cdot 10^5 and 1 \leq k \leq 10^9. p is a permutation of length n, and a is an array of positive integers of length n.
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
        
    #State: The output will be determined based on the maximum value between `resb` and `ress` for each iteration. If `resb` is greater than `ress`, "Bodya" will be printed; if `ress` is greater than `resb`, "Sasha" will be printed; otherwise, "Draw" will be printed. The specific values of `resb` and `ress` depend on the input values of `n`, `k`, `pb`, `ps`, `p`, and `a`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n, k, P_B, and P_S, a permutation p, and an array a. It then determines two paths, one starting from P_B and the other from P_S, and calculates the maximum possible sum of k consecutive elements along each path. Based on which path has the higher sum, it prints either "Bodya", "Sasha", or "Draw".

