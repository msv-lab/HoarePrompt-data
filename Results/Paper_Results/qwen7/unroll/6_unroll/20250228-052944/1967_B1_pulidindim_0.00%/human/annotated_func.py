#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2⋅10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 10^4, `n` and `m` are pairs of integers where 1 ≤ `n`, `m` ≤ 2⋅10^6 for each iteration of the loop, and `ans` is the accumulated result of the loop's computations for each `i` from 0 to `t-1`. After all iterations, the values of `n` and `m` for each iteration are processed to compute `ans` according to the given logic, and then printed as an integer.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads two integers \( n \) and \( m \) (with \( 1 \leq n, m \leq 2 \times 10^6 \)). It calculates and accumulates a result based on these inputs using a specific algorithm involving a while loop. Finally, it prints the computed result for each test case as an integer.

