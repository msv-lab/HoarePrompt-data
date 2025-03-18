#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: Output State: `a` is 2, `L` is [], `pow` is 16, `tot` is 12.
    #
    #Explanation: After all iterations of the loop, the list `L` becomes empty as the loop continues to process until `n` reaches 0. The variable `a` takes on the value of the last element added to `L`, which is 2. The variable `pow` is doubled in each iteration of the loop, starting from 8 after 3 iterations, and doubles again for each additional iteration until the loop completes. Since the loop processes until `L` is empty and `n` is 0, `pow` doubles for each of the 3 elements in `L`, resulting in `pow` being 16 (2^4). The variable `tot` is the sum of all elements in `L`, which is 2 + 2 + 2 = 6, and it continues to be incremented by `a` (which is 2) for each full iteration of `L` being processed, resulting in `tot` being 12 (6 + 6).
#Overall this is what the function does:The function processes multiple test cases, each containing integers \( t \), \( n \), and \( k \). For each test case, it calculates and prints a value based on the given \( n \) and \( k \). Specifically, it constructs a sequence \( L \) by repeatedly dividing \( n \) by 2 and subtracting the result from \( n \). It then iterates over this sequence, determining a value to print based on the position of \( k \) within the cumulative sum of elements in \( L \). The function does not return any value but prints the calculated value for each test case.

