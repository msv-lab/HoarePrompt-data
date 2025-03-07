#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: After all iterations, `n` and `m` are the final input integers provided during the last iteration, `t` is the initial input integer, `i` is `t - 1`, `count` is the final value it reaches after the loop completes, `ans` is the final computed value after all iterations, `m` is still greater than or equal to 1, `countmins` is `count - 1`, and `g` is the final value of `int(n / count) - countmins`. The loop terminates when `count` exceeds `m` or when `g` becomes less than `countmins`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6). It then performs a series of calculations to compute a value `ans` based on `n` and `m`. The final computed value `ans` is printed for each test case. After processing all test cases, the function terminates. The state after the function concludes includes the final values of `n`, `m`, `t`, `i`, `count`, `ans`, `countmins`, and `g` as described in the annotations, but the primary output is the printed values of `ans` for each test case.

