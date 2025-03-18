#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, and P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a list of n integers such that 1 ≤ p_i ≤ n, representing the permutation. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, representing the array of scores. The sum of values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop executes all the iterations, and for each test case, it prints either 'Bodya', 'Sasha', or 'Draw' based on the calculated scores. The variables `YES`, `NO`, `MOD`, and `alpha` remain unchanged. The variables `n`, `k`, `pb`, `ps`, `p`, `a`, `pathb`, `paths`, `resb`, `ress`, `preb`, and `pres` are updated and used within each iteration but are reset or reinitialized for the next test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes the number of elements `n`, the duration of the game `k`, the starting positions of Bodya `P_B` and Sasha `P_S`, a permutation list `p`, and a score list `a`. It calculates the maximum possible scores for Bodya and Sasha based on their paths through the permutation and the game duration. After processing, it prints 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if their scores are equal. The function does not return any values, and the variables `YES`, `NO`, `MOD`, and `alpha` remain unchanged throughout the execution. The state of other variables is reset for each new test case.

