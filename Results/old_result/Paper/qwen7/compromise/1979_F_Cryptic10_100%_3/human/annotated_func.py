#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 2 ≤ n ≤ 10^5. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: After all iterations of the loop, `vx` is a set containing exactly 2 elements, both being the last two elements of the original `vx` before the loop started; `p1` is a list of the original elements in `vx`; `p2` is a list containing all `v1` values appended according to the conditions inside the loop; `ops` is a list containing all tuples from the original operations but in reverse order; `v1` and `v2` are undefined.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and then a set of integers from 1 to `n`. It repeatedly removes pairs of integers from the set based on certain conditions and records the operations performed. After processing, it reconstructs the original set and applies the recorded operations in reverse order to produce a final sequence of integers. This sequence is then printed as the result.

