#State of the program right berfore the function call: t is a positive integer, and for each test case, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9. Additionally, p is a permutation of length n, and a is an array of positive integers of length n.
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
        
    #State: The output will be determined based on the comparison between `resb` and `ress`. If `resb` is greater than `ress`, "Bodya" will be printed; if `ress` is greater than `resb`, "Sasha" will be printed; otherwise, "Draw" will be printed. The specific values of `resb` and `ress` depend on the input values of `n`, `k`, `pb`, `ps`, `p`, and `a`.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( n \), \( k \), \( P_B \), \( P_S \), a permutation \( p \) of length \( n \), and an array \( a \) of positive integers of length \( n \). For each test case, it calculates two paths, one starting from \( P_B \) and the other from \( P_S \), and determines the maximum sum of \( k \) consecutive elements along each path. Based on the comparison of these sums, it prints either "Bodya", "Sasha", or "Draw".

