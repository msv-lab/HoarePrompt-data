#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each testcase, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. p is a list of n integers representing the permutation, where 1 ≤ p_i ≤ n for all i. a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all i.
def func():
    t = int(input())
    for i in range(t):
        n, k, b, s = list(map(int, input().split()))
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        b -= 1
        
        s -= 1
        
        sp = a[s]
        
        bp = a[b]
        
        bm = a[b] * k
        
        sm = a[s] * k
        
        for i in range(n):
            k -= 1
            if k == 0:
                break
            b = p[b] - 1
            s = p[s] - 1
            bm = max(bm, a[b] * k + bp)
            sm = max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: Output State: t is an input integer indicating the number of test cases. For each test case, the following variables are updated after the loop execution:
    #
    #- n, k, b, s are integers representing the length of lists p and a, a starting index, and another starting index respectively.
    #- p and a are lists of integers.
    #- After the loop, bm and sm are updated based on the maximum values calculated during the iterations.
    #- The loop prints 'Bodya' if bm is greater than sm, 'Sasha' if bm is less than sm, and 'Draw' if bm equals sm.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \(t\), \(n\), \(k\), and two indices \(b\) and \(s\). It also takes two lists, \(p\) and \(a\), both of length \(n\). For each test case, it calculates two values, \(bm\) and \(sm\), based on the elements of \(a\) and the permutations defined by \(p\). It then compares these values and prints 'Bodya', 'Sasha', or 'Draw' based on their relative sizes. The function does not return any value but outputs the result for each test case.

