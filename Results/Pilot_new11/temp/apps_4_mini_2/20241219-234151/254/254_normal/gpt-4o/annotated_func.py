#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_{i} ≤ 1500.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k1`, `k2`, and `k3` are integers such that 1 ≤ `k1`, `k2`, `k3` ≤ 1500. If `gcd_all` is equal to 1, 'YES' is printed. Otherwise, if `gcd_all` is greater than 1, 'NO' is printed.
#Overall this is what the function does:The function reads three integers (k1, k2, k3) from input, each ranging from 1 to 1500. It calculates the greatest common divisor (GCD) of k1 and k2, and then calculates the GCD of that result with k3. If the final GCD (gcd_all) is equal to 1, it prints 'YES', indicating that the three numbers are coprime. If gcd_all is greater than 1, it prints 'NO', indicating that there exists a common divisor greater than 1 among the three numbers. The function does not return any values directly. The program effectively checks for coprimality of the three input integers.

