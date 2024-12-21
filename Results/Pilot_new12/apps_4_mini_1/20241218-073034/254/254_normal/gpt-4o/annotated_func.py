#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_i ≤ 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k_1`, `k_2`, and `k_3` are integers such that 1 ≤ `k_i` ≤ 1500 for i = 1, 2, 3. If the greatest common divisor of `k_1`, `k_2`, and `k_3` (denoted as `gcd_all`) is equal to 1, then 'YES' is printed. Otherwise, if `gcd_all` is greater than 1, 'NO' is printed.
#Overall this is what the function does:The function reads three integers k1, k2, and k3 from user input, checks the greatest common divisor (GCD) of these integers, and prints 'YES' if their GCD is 1 (indicating that the numbers are coprime), or 'NO' if their GCD is greater than 1. This process requires the input values to be within the range of 1 to 1500. The function does not return any value and its output is solely based on the GCD calculation.

