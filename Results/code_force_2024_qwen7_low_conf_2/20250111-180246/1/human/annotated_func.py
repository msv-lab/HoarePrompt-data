#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice.
def func_1():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        k = 2 * k
        
        a = list(map(int, input().split()))
        
        occ = [0] * (n + 1)
        
        for x in a:
            occ[x] += 1
        
        g0, g1, g2 = [], [], []
        
        for i in range(1, n + 1):
            if occ[i] == 0:
                g0.append(i)
            elif occ[i] == 1:
                g1.append(i)
            else:
                g2.append(i)
        
        v = 0
        
        output = []
        
        for x in g2:
            if v < k:
                output.append(f'{x} {x}')
                v += 2
        
        for x in g1:
            if v < k:
                output.append(f'{x}')
                v += 1
        
        print(' '.join(output))
        
        v = 0
        
        output = []
        
        for x in g0:
            if v < k:
                output.append(f'{x} {x}')
                v += 2
        
        for x in g1:
            if v < k:
                output.append(f'{x}')
                v += 1
        
        print(' '.join(output))
        
    #State of the program after the  for loop has been executed: `t` is an input integer within the range \(1 \leq t \leq 5000\), `n` is an integer from the input, `k` is \(2 \times n\), `a` is a list of integers from the input, `occ` is a list of \(n + 1\) elements where all elements are 0, `g0` is a list of integers from 1 to `n` where `occ[i] == 0`, `g1` is a list of integers from 1 to `n` where `occ[i] == 1`, `g2` is a list of integers from 1 to `n` where `occ[i] > 1`, `v` is the final value of `v` after all iterations, `output` is a list of string representations of integers and pairs of integers as described in the loop logic, `i` is the length of `occ` (which is `n + 1`).
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the number of test cases \(t\), the values of \(n\) and \(k\), and an array \(a\) of \(2n\) integers where each integer from 1 to \(n\) appears exactly twice. It then identifies elements in the array \(a\) based on their occurrences (0, 1, or more than 1 times) and constructs an output list according to specific rules. Specifically, it selects elements from the groups with occurrences greater than 1 and exactly 1, ensuring the total count of selected elements is at most \(2k\). Finally, it prints the constructed output list for each test case. The function does not return anything explicitly but prints the results directly.

