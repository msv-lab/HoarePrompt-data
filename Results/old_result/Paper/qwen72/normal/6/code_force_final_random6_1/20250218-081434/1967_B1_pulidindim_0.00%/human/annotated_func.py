#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: `n` and `m` are the final input integers, `t` is the input integer, `i` is `t - 1`, `count` is `m + 1`, `ans` is `n + sum((n / k - (k - 1)) / k + 1 for k in range(2, m + 1))`, `countmins` is `m - 1`, `g` is `n / m - (m - 1)`. If `g` is less than `countmins`, the loop breaks.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `m` from the input. It then calculates a value `ans` based on `n` and `m` using a specific formula and prints the integer value of `ans`. The function does not return any value. After the function concludes, `n` and `m` are the final input integers for the last test case, `t` is the total number of test cases, `i` is `t - 1`, `count` is `m + 1`, and `ans` is the final calculated value for the last test case.

