#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_i ≤ 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k_1`, `k_2`, and `k_3` are integers within the range 1 to 1500. If `gcd_all` is 1, then 'YES' is printed. Otherwise, if `gcd_all` is greater than 1, 'NO' is printed.
#Overall this is what the function does:The function reads three integers, k1, k2, and k3, from user input, which are constrained to be within the range of 1 to 1500. It computes the greatest common divisor (GCD) of these integers. If the GCD of the three integers is 1, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any values, and it directly prints the outcome. The function does not handle invalid input (e.g., non-integer values or numbers outside the specified range), which could lead to runtime errors. Additionally, it assumes input as space-separated integers without error handling for improper formatting.

