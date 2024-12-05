#State of the program right berfore the function call: k_1, k_2, and k_3 are integers such that 1 ≤ k_i ≤ 1500 for i = 1, 2, 3.
def func():
    k1, k2, k3 = map(int, input().split())
    gcd_k1_k2 = math.gcd(k1, k2)
    gcd_all = math.gcd(gcd_k1_k2, k3)
    if (gcd_all == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`k_1`, `k_2`, `k_3` are integers such that 1 ≤ `k_1`, `k_2`, `k_3` ≤ 1500. If `gcd_all` is equal to 1, then 'YES' has been printed. Otherwise, if `gcd_all` is greater than 1, then 'NO' was printed.
#Overall this is what the function does:The function accepts three integers, calculates their GCD, and prints 'YES' if they are coprime (GCD is 1), or 'NO' if they are not coprime (GCD is greater than 1).

