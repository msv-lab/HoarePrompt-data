#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_i ≤ 1500 for i in {1, 2, 3}.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k1`, `k2`, `k3` are integers with values as input from the user. If `gcd_all` is 1, then `k1`, `k2`, and `k3` are pairwise coprime. Otherwise, if `gcd_all` is greater than 1, the output is 'NO'.
#Overall this is what the function does:The function accepts three integers `k1`, `k2`, and `k3` through user input. It calculates the greatest common divisor (GCD) of these integers and checks if they are pairwise coprime. If the GCD of all three integers is 1, it prints 'YES'; otherwise, it prints 'NO'. There are no parameters passed to the function, and the only output is the result of the GCD check.

