#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers such that 1 ≤ a_i ≤ 10^9 for all i.
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
        
    #State: Output State: The output state consists of multiple lines, each line representing the result ('Bodya', 'Sasha', or 'Draw') for each test case after executing the loop. For each test case, the loop updates the maximum values `bm` and `sm`, and prints 'Bodya' if `bm` is greater than `sm`, 'Sasha' if `bm` is less than `sm`, and 'Draw' if they are equal.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads in values for \( t \), \( n \), \( k \), \( P_B \), \( P_S \), a permutation \( p \), and an array \( a \). It then calculates two scores, `bm` and `sm`, based on the values of elements in \( a \) and their positions in \( p \), adjusted by \( k \). After iterating through the permutation, it compares `bm` and `sm` and prints either 'Bodya', 'Sasha', or 'Draw' based on which score is higher or if they are equal.

