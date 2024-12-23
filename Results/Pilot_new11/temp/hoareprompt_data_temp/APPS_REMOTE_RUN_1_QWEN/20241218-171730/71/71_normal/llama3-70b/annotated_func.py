#State of the program right berfore the function call: n is an integer such that 0 ≤ n ≤ 2,000,000,000, and k is an integer such that 1 ≤ k ≤ 9.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `w` is the number of times `n` was divided by 10 until `n` became divisible by \(10^k\), `n` is the integer quotient of the original value of `n` divided by \(10^w\) and is divisible by \(10^k\)
    print(w)
#Overall this is what the function does:The function takes no explicit parameters but reads two integers `n` and `k` from standard input, where `0 ≤ n ≤ 2,000,000,000` and `1 ≤ k ≤ 9`. It then repeatedly divides `n` by 10 until `n` becomes divisible by \(10^k\). During this process, it counts the number of divisions performed and stores this count in the variable `w`. After the loop terminates, the function prints the value of `w`, which represents the number of times `n` had to be divided by 10 to make it divisible by \(10^k\). The final state of the program is that `n` is now divisible by \(10^k\) and `w` holds the required count of divisions.

