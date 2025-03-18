#State of the program right berfore the function call: There are three integers, k1, k2, and k3, representing the time intervals of the garlands, such that 1 <= ki <= 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `k1` is an input integer, `k2` is an input integer, `k3` is an input integer, 1 <= `k1` <= 1500, 1 <= `k2` <= 1500, 1 <= `k3` <= 1500, `gcd_k1_k2` is the greatest common divisor of `k1` and `k2`, `gcd_all` is the greatest common divisor of `gcd_k1_k2` and `k3`, if `gcd_all` is 1, 'YES' has been printed, otherwise 'NO' has been printed to the output.
#Overall this is what the function does:The function reads three integers from input, checks if they are coprime, and prints 'YES' if their greatest common divisor is 1, and 'NO' otherwise, but may fail with an error if the input is not as expected

