#State of the program right berfore the function call: k_1, k_2, and k_3 are positive integers such that 1 ≤ k_i ≤ 1500.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k1` is an integer between 1 and 1500, `k2` is an integer between 1 and 1500, `gcd_k1_k2` is the GCD of `k1` and `k2`, `gcd_all` is the GCD of `gcd_k1_k2` and `k3`. If `gcd_all` equals 1, the program continues normally. If `gcd_all` does not equal 1, 'NO' is printed.
#Overall this is what the function does:The function takes three positive integers \(k_1\), \(k_2\), and \(k_3\) as input, each constrained to be between 1 and 1500. It calculates the greatest common divisor (GCD) of \(k_1\) and \(k_2\), then finds the GCD of this result and \(k_3\). If the final GCD is 1, the function prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value; instead, it prints the result directly.

