#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. p is a permutation of length n consisting of integers from 1 to n. a is an array of length n consisting of integers such that 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The values of `t`, `n`, `k`, `P_B`, `P_S`, `p`, `a`, `MOD`, and `alpha` remain unchanged. The variables `pathb`, `paths`, `resb`, `ress`, `preb`, and `pres` are reset and recalculated for each test case. After all iterations of the loop, the final values of `pathb`, `paths`, `resb`, `ress`, `preb`, and `pres` are undefined as they are reinitialized and used within each test case loop. The loop prints 'Bodya', 'Sasha', or 'Draw' for each test case based on the calculated values of `resb` and `ress`.
#Overall this is what the function does:The function processes multiple test cases, each defined by the parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it calculates the maximum possible sum of elements in two different paths starting from `P_B` and `P_S` in the permutation `p`, considering the array `a` and the limit `k`. The function then compares these sums and prints 'Bodya' if the sum from `P_B` is greater, 'Sasha' if the sum from `P_S` is greater, or 'Draw' if they are equal. The function does not return any values; it only prints the result for each test case. After processing all test cases, the function completes and the final state of the program is undefined for the variables `pathb`, `paths`, `resb`, `ress`, `preb`, and `pres`, as they are reinitialized for each test case. The input parameters `t`, `n`, `k`, `P_B`, `P_S`, `p`, and `a` remain unchanged.

