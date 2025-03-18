#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 2 ≤ n ≤ 10^5. Additionally, the sum of n over all test cases does not exceed 10^5.
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
        
    #State: After all iterations, `ops` will be an empty list, `p1` will contain the elements of `vx` in their original order, and `p2` will contain all the elements that were appended during the iterations in reverse order of their appearance.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( t \) and \( n \). For each test case, it maintains a set of integers and performs operations based on user-provided inputs. After processing, it reconstructs and prints a sequence of integers based on the operations performed. The final output is a sequence of integers for each test case, formatted as a space-separated string.

