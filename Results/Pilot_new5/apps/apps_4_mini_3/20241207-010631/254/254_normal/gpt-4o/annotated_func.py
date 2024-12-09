#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_i ≤ 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k_1`, `k_2`, and `k_3` are integers such that 1 ≤ `k_i` ≤ 1500 for i = 1, 2, 3; if the greatest common divisor of `k_1` and `k_2`, and subsequently `k_3`, is 1, then 'YES' is printed. Otherwise, if the greatest common divisor is greater than 1, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `k1`, `k2`, and `k3` from the user input, each within the range of 1 to 1500. It calculates the greatest common divisor (GCD) of these three integers and prints 'YES' if the GCD is 1 (indicating that the numbers are coprime), and 'NO' if the GCD is greater than 1. The function does not return any value.

