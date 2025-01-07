#State of the program right berfore the function call: The function takes no explicit inputs, but it is implied that there are three positive integers k1, k2, and k3, representing the time intervals of the garlands, such that 1 <= ki <= 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `k1` is an integer between 1 and 1500, `k2` is an integer between 1 and 1500, `k3` is an integer between 1 and 1500, `gcd_k1_k2` is the greatest common divisor of `k1` and `k2`, `gcd_all` is the greatest common divisor of `gcd_k1_k2` and `k3`. If `gcd_all` is 1, the string 'YES' has been printed. If `gcd_all` is greater than 1, the string 'NO' has been printed.
#Overall this is what the function does:The function determines whether the greatest common divisor (GCD) of three implicitly provided positive integers `k1`, `k2`, and `k3`, each between 1 and 1500, is 1. It prints 'YES' if the GCD is 1, indicating that the numbers are coprime, and 'NO' otherwise. The function modifies the program state by printing a string to the console based on the GCD calculation. The input integers are obtained from standard input, implying user interaction. The function does not handle invalid inputs (e.g., non-integer or out-of-range values), which could lead to errors or unexpected behavior. After execution, the program state includes the printed result ('YES' or 'NO') and the calculated GCD value, although the latter is not explicitly returned or stored. The original input values (`k1`, `k2`, and `k3`) are not modified. Potential edge cases, such as inputs outside the specified range or non-integer inputs, are not handled by the function.

