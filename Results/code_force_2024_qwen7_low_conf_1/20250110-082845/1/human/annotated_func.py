#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State of the program after the  for loop has been executed: Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers `n` and `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. It then categorizes these integers into three groups based on their occurrences: `g0` for integers appearing 0 times, `g1` for integers appearing 1 time, and `g2` for integers appearing more than 1 time. Finally, it generates an output string for each group and prints it. Specifically, it ensures that the number of elements printed from each group does not exceed `k` while maintaining the required format.

