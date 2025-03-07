#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
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
        
    #State: The output state after all iterations is the sequence of integers printed for each test case, where each integer is the final value of `ans` after processing the corresponding `n` and `m`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `m`. For each test case, it calculates a specific integer value based on the given `n` and `m`, and prints this value. The final state of the program is the sequence of integers printed, one for each test case.

