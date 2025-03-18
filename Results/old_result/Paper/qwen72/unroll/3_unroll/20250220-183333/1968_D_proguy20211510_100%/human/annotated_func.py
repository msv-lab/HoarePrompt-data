#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. For each test case, n, k, P_B, and P_S are integers such that (1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5) and (1 ≤ k ≤ 10^9), representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a permutation of length n, consisting of distinct integers from 1 to n. a is an array of length n, where each element a_i is a positive integer (1 ≤ a_i ≤ 10^9). The sum of values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop executes all iterations, and for each test case, it prints either 'Bodya', 'Sasha', or 'Draw' based on the comparison of `resb` and `ress`. The values of `n`, `k`, `pb`, `ps`, `p`, `a`, `pathb`, `paths`, `vis`, `resb`, `ress`, `preb`, and `pres` are updated within the loop, but their final values after the loop are not explicitly defined in the output state. The loop itself does not modify the values of `YES`, `NO`, `MOD`, or `alpha`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it calculates the maximum possible score for two players, Bodya and Sasha, based on their movements through a permutation `p` and the values in array `a`. The function then prints the result of the game for each test case, which can be 'Bodya', 'Sasha', or 'Draw', depending on which player has the higher score or if they have the same score. The function does not return any values, and it does not modify the global variables `YES`, `NO`, `MOD`, or `alpha`.

