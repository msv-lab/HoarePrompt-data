#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 2 ≤ n ≤ 10^5. It is guaranteed that the sum of n over all test cases does not exceed 10^5.
def func():
    q = lambda d: print('? %d' % d, flush=True) or map(int, input().split())
    for _ in range(int(input())):
        vx, ops = set(i for i in range(1, int(input()) + 1)), []
        
        while len(vx) > 2:
            v1, v2 = q(len(vx) - 2)
            vx.remove(v1)
            if v2 > 0:
                ops += [(v1, v2)]
            else:
                v3, _ = q(0)
                vx.remove(v3)
                ops += [(v3, 0), (v1, 0)]
        
        p1, p2 = list(vx), []
        
        for v1, v2 in ops[::-1]:
            (p2 if p1[-1] == v2 else p1).append(v1)
        
        print('! %s' % ' '.join(map(str, p1[::-1] + p2)), flush=True)
        
    #State: t tests are performed. For each test, two permutations p1 and p2 are printed such that p1 is a permutation of numbers from 1 to n-2, and p2 is a permutation of numbers n-1 and n. The operations to transform the initial set vx into these permutations are recorded in ops and applied in reverse order to generate p1 and p2.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and performs a series of operations to transform a set of numbers into two permutations, `p1` and `p2`. The function then prints the final permutations `p1` and `p2` along with the operations that were applied to generate them. The function does not return any value but prints the results for each test case.

