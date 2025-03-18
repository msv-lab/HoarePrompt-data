#State of the program right berfore the function call: k_1, k_2, and k_3 are positive integers such that 1 ≤ k_i ≤ 1500 for i in {1, 2, 3}.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `gcd_k1_k2` is the GCD of `k1` and `k2`, `k1` and `k2` are integers read from input, `k3` is an integer read from input, `gcd_all` is the GCD of `gcd_k1_k2`, `k1`, and `k2`. If the GCD of `gcd_k1_k2`, `k1`, `k2`, and `k3` is 1, the function does not return anything (implying no change). Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function reads three positive integers \( k_1 \), \( k_2 \), and \( k_3 \) from the input, computes the GCD of these three integers, and prints 'YES' if the GCD is 1, and 'NO' otherwise.

