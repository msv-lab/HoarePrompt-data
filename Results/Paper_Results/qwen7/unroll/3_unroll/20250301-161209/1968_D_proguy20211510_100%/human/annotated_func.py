#State of the program right berfore the function call: t is a positive integer, and for each test case, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9. p is a permutation of length n, and a is an array of positive integers of length n.
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
        
    #State: Output State: The output will be determined based on the comparison of `resb` and `ress` after processing each test case. `resb` represents the maximum possible sum Sasha can achieve starting from `pb`, and `ress` represents the maximum possible sum Bodya can achieve starting from `ps`. The loop will print "Bodya" if `resb` is greater than `ress`, "Sasha" if `ress` is greater than `resb`, and "Draw" if they are equal.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes a permutation `p` of length `n`, an array `a` of length `n`, and four positive integers `n`, `k`, `P_B`, and `P_S`. It calculates the maximum possible sums `resb` and `ress` that two players, Bodya and Sasha, can achieve starting from positions `P_B` and `P_S` respectively, over `k` steps. Based on these sums, it prints "Bodya", "Sasha", or "Draw" to indicate which player has the higher sum or if they are equal.

