#State of the program right berfore the function call: no input parameters, but the input are three integers k_1, k_2, and k_3 which are the time intervals of the garlands, where 1 <= k_1, k_2, k_3 <= 1500.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k1` is an integer between 1 and 1500, `k2` is an integer between 1 and 1500, `k3` is an integer between 1 and 1500, `gcd_k1_k2` is the greatest common divisor of `k1` and `k2`, and `gcd_all` is the greatest common divisor of `gcd_k1_k2` and `k3`. If `gcd_all` equals 1, 'YES' has been printed. If `gcd_all` is greater than 1, 'NO' has been printed to the console.
#Overall this is what the function does:The function reads three integers k_1, k_2, and k_3 from user input, representing time intervals of garlands, where 1 <= k_1, k_2, k_3 <= 1500. It calculates the greatest common divisor (GCD) of k_1 and k_2, and then the GCD of the result with k_3. If the final GCD is 1, it prints 'YES', indicating that the time intervals are coprime, otherwise, it prints 'NO'. The function does not return any value but modifies the output console with either 'YES' or 'NO'. All potential edge cases, such as the input values being within the specified range and the GCD calculation, are implicitly handled by the math.gcd function. The function does not validate the input range, so it will still calculate and print a result even if the input values are outside the range 1-1500.

