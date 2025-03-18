#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers such that 1 ≤ a_i ≤ 10^9 for all i.
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
        
    #State: Output State: After the loop executes all the iterations, `resb` will hold the highest value obtained from the loop's iterations, `ress` will be 0, `preb` will be the sum of all elements in `pathb`, `pres` will be 0, `i` will be equal to `len(pathb)`, and `curr` will be the final computed value before the loop exits. Additionally, `resb` will be greater than or equal to `ress`.
    #
    #To explain this in more detail:
    #- `resb` retains the highest value it was updated to during any iteration of the loop.
    #- `ress` is reset to 0 after the loop completes because no further comparisons are made.
    #- `preb` accumulates the sum of all elements in `pathb` as the loop progresses.
    #- `pres` is reset to 0 at the start of each outer loop iteration.
    #- `i` will be equal to `len(pathb)` after the loop exits, indicating the last index processed.
    #- `curr` will be the final computed value before the loop exits, which is compared against `resb` and `ress` during each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, k, P_B, P_S, a permutation p, and an array a. For each test case, it constructs two paths based on the permutation and calculates the maximum possible values for these paths under a given constraint k. It then compares these values and prints 'Bodya' if the first path's value is higher, 'Sasha' if the second path's value is higher, or 'Draw' if both values are equal. The function does not return any value but prints the result for each test case.

