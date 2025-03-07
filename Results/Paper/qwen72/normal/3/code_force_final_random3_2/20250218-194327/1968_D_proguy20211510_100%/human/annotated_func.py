#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a list of n integers such that 1 ≤ p_i ≤ n, representing the permutation. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, representing the array of scores. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all the iterations, `n`, `k`, `p`, `a`, `pb`, `ps`, `pathb`, `paths`, and `vis` remain unchanged. `preb` is the sum of the first `min(k, len(pathb))` elements of `pathb`. `resb` is the maximum value of `preb + pathb[i] * (k - i)` for all `i` from 0 to `min(k, len(pathb)) - 1` where `k >= i`. `pres` is the sum of the first `min(k, len(paths))` elements of `paths`. `ress` is the maximum value of `pres + paths[i] * (k - i)` for all `i` from 0 to `min(k, len(paths)) - 1` where `k >= i`. The final output is 'Bodya' if `resb` is greater than `ress`, 'Sasha' if `ress` is greater than `resb`, and 'Draw' if `resb` is equal to `ress`.
#Overall this is what the function does:The function `func` processes multiple game scenarios defined by user inputs. Each scenario involves two players, Bodya and Sasha, who move through a permutation of integers `p` and collect scores from an array `a` over a specified duration `k`. The function determines the winner based on the maximum score each player can achieve within the game duration, starting from their respective positions `P_B` and `P_S`. If Bodya's maximum score is greater than Sasha's, the function outputs 'Bodya'. If Sasha's maximum score is greater, it outputs 'Sasha'. If both have the same maximum score, it outputs 'Draw'. The function does not return any values but prints the result for each test case.

