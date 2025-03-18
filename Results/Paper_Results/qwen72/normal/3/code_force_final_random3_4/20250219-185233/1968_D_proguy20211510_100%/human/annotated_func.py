#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a permutation of length n, and a is an array of n integers such that 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: All iterations of the loop have completed. `pres` is the sum of the first `min(k, len(paths))` elements of `paths`, `preb` is the sum of all elements in `pathb`, `resb` is the maximum value of `preb + pathb[i] * (k - i)` for all `i` from 0 to `min(k, len(pathb)) - 1`, `ress` is the maximum value of `pres + paths[j] * (k - j)` for all `j` from 0 to `min(k, len(paths)) - 1`, `i` is `min(k, len(paths)) - 1`, `paths` and `pathb` have been fully traversed up to `min(k, len(paths))` and `min(k, len(pathb))` respectively, and the final comparison between `resb` and `ress` has been made, determining the winner or a draw. The values of `n`, `k`, `pb`, `ps`, `p`, `a`, and `vis` remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it determines the winner of a game between two players, Bodya and Sasha, based on their paths through a permutation `p` and an array `a`. The function prints 'Bodya' if Bodya's maximum score is higher, 'Sasha' if Sasha's maximum score is higher, and 'Draw' if their scores are equal. The function does not return any values; it only prints the results for each test case. After the function concludes, the input variables `n`, `k`, `P_B`, `P_S`, `p`, and `a` remain unchanged.

