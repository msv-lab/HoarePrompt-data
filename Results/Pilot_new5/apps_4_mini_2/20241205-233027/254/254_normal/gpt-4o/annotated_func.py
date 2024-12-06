#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_i ≤ 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k1`, `k2`, and `k3` are integers satisfying 1 ≤ `k1`, `k2`, `k3` ≤ 1500. If the greatest common divisor of `k1`, `k2`, and `k3` is 1, then 'YES' is printed. Otherwise, if the greatest common divisor is greater than 1, it indicates that `k1`, `k2`, and `k3` share a common factor.
#Overall this is what the function does:The function reads three integers `k1`, `k2`, and `k3` from user input (each between 1 and 1500) and calculates their greatest common divisor (GCD). It prints 'YES' if the GCD is 1 (indicating that the numbers are coprime), and 'NO' if the GCD is greater than 1 (indicating that they share a common factor). The function does not accept any parameters and relies on user input for its operation.

