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
        
    #State: The output state will consist of two lists concatenated together and printed in reverse order for each test case. The first list contains the last two elements of the set `vx` after removing elements according to the operations defined in the `ops` list. The second list is constructed by reversing the operations defined in `ops`. The entire output is formatted as '! <result>' where `<result>` is a space-separated list of integers.
#Overall this is what the function does:The function processes multiple test cases, each involving a set of integers. For each test case, it repeatedly queries the user for pairs of integers, removes them from the set, and records operations. After processing all pairs, it reconstructs and prints a specific sequence of integers based on the recorded operations and the remaining elements in the set. The final output consists of two lists concatenated and printed in reverse order for each test case.

