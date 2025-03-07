#State of the program right berfore the function call: The function `func` does not take any parameters, but based on the problem description, it is implied that the function should take parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. Here, `n` is a positive integer representing the length of the permutation, `k` is a positive integer representing the number of turns in the game, `P_B` and `P_S` are positive integers representing the starting positions of Bodya and Sasha respectively, such that 1 <= P_B, P_S <= n. `p` is a permutation of length `n` containing distinct integers from 1 to `n`, and `a` is an array of length `n` containing positive integers, each between 1 and 10^9.
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
        
    #State: The loop has completed all iterations, or it broke early if `k` was less than the length of `paths` at any point. `i` is equal to the length of `paths` minus 1, or the value of `i` when the loop broke. `pres` is the sum of all elements in `paths` up to the point where the loop completed or broke. `curr` is the final value of `pres + paths[-1] * (k - (len(paths) - 1))`, or the value calculated up to the point where the loop broke. `ress` is the maximum value encountered in the expression `pres + paths[i] * (k - i)` for all `i` from 0 to the length of `paths` minus 1, or the maximum value calculated up to the point where the loop broke. If `resb` is greater than `ress`, then `resb` is greater than `ress`. Otherwise, `ress` is greater than or equal to `resb`.
#Overall this is what the function does:The function `func` reads input from the user to simulate a game between Bodya and Sasha. It takes no explicit parameters but reads `n` (length of the permutation), `k` (number of turns), `P_B` (Bodya's starting position), `P_S` (Sasha's starting position), `p` (a permutation of length `n`), and `a` (an array of length `n` with positive integers). The function calculates the maximum possible scores for Bodya and Sasha based on their paths through the permutation and the values in the array `a`. After `k` turns, it prints 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if their scores are equal. The function does not return any value but prints the result directly.

