#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 \cdot 10^5, and the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i in the list.
def func():
    t = int(input())
    for j in range(t):
        b = input().split()
        
        n = int(b[0])
        
        k = int(b[1])
        
        l = list(map(int, input().split()))
        
        suf = []
        
        suf.append(0)
        
        for i in range(n):
            suf.append(suf[i] + l[i])
        
        smin = [0]
        
        for i in range(n):
            if suf[i + 1] < smin[i]:
                smin.append(suf[i + 1])
            else:
                smin.append(smin[i])
        
        sm = -111
        
        for i in range(n + 1):
            if suf[i] - smin[i] > sm or sm == -111:
                sm = suf[i] - smin[i]
        
        sm = 2 ** k * sm - sm
        
        sm += suf[n]
        
        if sm < 0:
            a = abs(sm) // (10 ** 9 + 7)
            sm += (a + 1) * (10 ** 9 + 7)
        else:
            sm = sm % (10 ** 9 + 7)
        
        print(sm)
        
    #State: sm is an integer calculated based on the final values of t, n, k, and l after all iterations of the loop, adjusted to ensure it is non-negative and within the range modulo \(10^9 + 7\).
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( n \) and \( k \), and a list \( l \) of \( n \) integers. It calculates a value \( sm \) based on these inputs using suffix sums and minimum suffix sums, adjusts \( sm \) to ensure it is non-negative and within the range modulo \( 10^9 + 7 \), and prints the result for each test case.

