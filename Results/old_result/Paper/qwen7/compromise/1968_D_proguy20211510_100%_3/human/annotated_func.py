#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers such that 1 ≤ a_i ≤ 10^9 for all i.
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
        
    #State: Output State: The loop will continue to execute until all inputs provided by the user are processed. After all iterations, the following conditions will hold:
    #
    #- `i` will be equal to the length of `paths`.
    #- `k` will be an integer less than or equal to the length of `paths`.
    #- `curr` will hold the value of `pres + paths[len(paths) - 1] * (k - len(paths) + 1)`, which represents the final calculation of `curr` when `k` equals the length of `paths`.
    #- `pres` will be the sum of all elements in the `paths` list.
    #- `ress` will contain the maximum value between its initial value and all the calculated `curr` values during the loop iterations. If `resb` is greater than `ress`, `ress` will be updated to the maximum value between `ress` and `resb`.
    #
    #If `resb` is greater than `ress`, the final output will be 'Bodya'. Otherwise, if `ress` is greater than `resb`, the final output will be 'Sasha'. If both `resb` and `ress` are equal, the final output will be 'Draw'.
    #
    #In summary, after all iterations, the decision ('Bodya', 'Sasha', or 'Draw') will be based on the comparison between `resb` and `ress`, with `resb` and `ress` being updated according to the calculations performed within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of positive integers \( n \), \( k \), \( P_B \), \( P_S \), a permutation \( p \) of length \( n \), and an array \( a \) of positive integers. For each test case, it constructs two paths based on the permutations and calculates the maximum possible sums for these paths under a given constraint \( k \). Based on the comparison of these sums, it outputs either 'Bodya', 'Sasha', or 'Draw' for each test case.

