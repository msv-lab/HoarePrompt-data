#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
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
        
    #State: `t` is unchanged. `n` and `m` are the values from the last test case. `count` is the final count value from the last test case. `ans` is the final answer printed for the last test case. `g` is the last computed value of `g` in the last test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two positive integers `n` and `m`. It then calculates and prints an integer value `ans` based on the provided `n` and `m`. The calculation involves iterating and updating a count and a value `g` until a certain condition is met, and the final result for each test case is printed as an integer.

