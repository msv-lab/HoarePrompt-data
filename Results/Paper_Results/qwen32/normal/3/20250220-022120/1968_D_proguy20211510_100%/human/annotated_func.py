#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each element p_i satisfies 1 <= p_i <= n. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9. The sum of values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The final output state is determined by the last test case processed. Specifically, `resb` and `ress` will hold the maximum scores for `pathb` and `paths` respectively, and the program will print "Bodya", "Sasha", or "Draw" based on the comparison of `resb` and `ress`. All other variables (`vis`, `pathb`, `paths`, `pb`, `ps`, `n`, `k`, `p`, `a`) will reflect the state of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `P_B`, and `P_S`, and lists `p` and `a`. For each test case, it calculates the maximum possible score for two players, Bodya and Sasha, based on their paths and the values in list `a`. It then prints "Bodya" if Bodya's score is higher, "Sasha" if Sasha's score is higher, or "Draw" if their scores are equal.

