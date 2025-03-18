#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, P_B, and P_S are integers satisfying 1 ≤ P_B, P_S ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of n positive integers.
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
            bm += max(bm, a[b] * k + bp)
            sm += max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: Output State: The output state depends on the input values for each iteration of the loop. For each input set, the output will either be 'Bodya', 'Sasha', or 'Draw' based on the comparison of `bm` and `sm`. The final output state will be a sequence of these strings corresponding to each input set provided.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( t \), \( n \), \( k \), and two indices \( P_B \) and \( P_S \), along with a permutation \( p \) and an array \( a \) of length \( n \). For each test case, it calculates two values, \( bm \) and \( sm \), based on the elements of \( a \) and the indices \( P_B \) and \( P_S \) under certain transformations. After processing all test cases, it prints 'Bodya', 'Sasha', or 'Draw' for each test case depending on the comparison between \( bm \) and \( sm \).

