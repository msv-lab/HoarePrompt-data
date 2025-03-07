#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^6. Additionally, the sum of all n and the sum of all m across all test cases do not exceed 2 · 10^6.
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
        
    #State: After executing all iterations, `t` test cases will be processed, and for each test case, the final value of `ans` will be printed. The variables `n`, `m`, `count`, and `g` will not retain their values after each iteration of the outer loop as they are recalculated or reinitialized within each loop. The state of `t` remains unchanged as it only dictates the number of test cases.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, performs a series of calculations, and prints a result based on these values. The function processes each test case independently and does not retain any state between them.

