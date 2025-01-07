#State of the program right berfore the function call: k_1, k_2, and k_3 are positive integers such that 1 ≤ k_i ≤ 1500 for i in {1, 2, 3}.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k1` is an integer between 1 and 1500, `k2` is an integer between 1 and 1500, `k3` is an integer between 1 and 1500, `gcd_all` is the GCD of `gcd_k1_k2` and `k3`. If `gcd_all` is 1, the function continues without change. If `gcd_all` is not 1, the function prints 'NO'.
#Overall this is what the function does:The function accepts no parameters directly but reads three integers \( k_1 \), \( k_2 \), and \( k_3 \) from standard input, where each integer is constrained to be between 1 and 1500 inclusive. It calculates the greatest common divisor (GCD) of \( k_1 \) and \( k_2 \), then calculates the GCD of the result with \( k_3 \). Based on whether the final GCD is 1, the function prints either 'YES' or 'NO'. The function returns no value explicitly but affects the output through printing. Potential edge cases include inputs that are exactly 1 or 1500, as well as any values that might cause integer overflow (though given the constraints, this is unlikely). The function handles all valid inputs within the specified range correctly.

