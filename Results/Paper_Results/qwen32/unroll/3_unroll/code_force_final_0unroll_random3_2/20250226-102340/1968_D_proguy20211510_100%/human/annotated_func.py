#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n. a is a list of n integers where each a_i is an integer such that 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: After all iterations, the variables `t`, `n`, `k`, `pb`, `ps`, `p`, `a`, `pathb`, `paths`, `vis`, `resb`, `ress`, `preb`, and `pres` will no longer hold their values from the last iteration. The variable `t` will be reduced to 0 as the loop has finished executing. The lists `pathb` and `paths` will be empty, and `vis` will be a list of zeros with length `n` from the last test case. The variables `resb`, `ress`, `preb`, and `pres` will hold the final results from the last test case's computations. The values of `YES`, `NO`, `MOD`, and `alpha` will remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it evaluates two paths starting from given positions in a list and calculates the maximum possible score based on a given number of steps. It then compares the scores of these two paths and prints the result indicating whether "Bodya" wins, "Sasha" wins, or if it is a "Draw".

