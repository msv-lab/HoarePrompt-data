#State of the program right berfore the function call: The function `func` is expected to be called with the necessary input parameters as described in the problem statement, but the actual parameters are not provided in the function definition. The correct function definition should include parameters for the number of test cases `t`, the length of the permutation `n`, the duration of the game `k`, the starting positions of Bodya and Sasha `P_B` and `P_S`, the permutation `p`, and the array `a`. Each parameter should adhere to the constraints: `1 <= t <= 10^4`, `1 <= P_B, P_S <= n <= 2 * 10^5`, `1 <= k <= 10^9`, `1 <= p_i <= n`, and `1 <= a_i <= 10^9`.
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
        
    #State: `MOD` is 1000000007, `alpha` is 'abcdefghijklmnopqrstuvwxyz', `YES` is 'YES', `NO` is 'NO'.
#Overall this is what the function does:The function `func` processes multiple test cases, each involving a permutation `p` and an array `a`. It simulates a game where two players, Bodya and Sasha, start at different positions in the permutation and move according to the rules defined by the permutation and the array. The function calculates the maximum score each player can achieve within a given number of moves `k` and determines the winner. For each test case, it prints "Bodya" if Bodya wins, "Sasha" if Sasha wins, or "Draw" if the scores are equal. The function does not return any value.

