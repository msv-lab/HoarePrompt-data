#State of the program right berfore the function call: a and b are integers such that 0 ≤ a, b < 998244353, and MOD is a constant integer equal to 998244353.
def func_1(a, b):
    return a * b % MOD
    #`The program returns (a * b) % 998244353`
#Overall this is what the function does:The function `func_1` accepts two integer parameters `a` and `b`, both of which must satisfy \(0 \leq a, b < 998244353\), and returns the result of \((a * b) \% 998244353\). The function ensures that the product of `a` and `b` is taken modulo \(998244353\) to prevent overflow and to work within the specified range. There are no additional actions performed beyond the multiplication and modulo operation. The function handles the given constraints and performs the required computation accurately.

#State of the program right berfore the function call: a and b are non-negative integers, with \( b > 0 \). The function `func_1` is assumed to exist and correctly implement the multiplication operation under modular arithmetic, specifically `func_1(x, y)` returns \( x \times y \mod 998244353 \).
def func_2(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = func_1(res, a)
        
        a = func_1(a, a)
        
        b >>= 1
        
    #State of the program after the loop has been executed: res is \( a^{b} \), a is \( a^{2^k} \) where \( k \) is the number of times the loop ran, b is 0.
    return res
    #The program returns res which is \(a^b\), where \(a\) is \(a^{2^k}\) and \(b\) is 0, and \(k\) is the number of times the loop ran
#Overall this is what the function does:The function `func_2` accepts two parameters `a` and `b`, both of which are non-negative integers with \( b > 0 \). The function calculates \( a^b \mod 998244353 \) using an efficient exponentiation by squaring algorithm. Specifically, it iteratively squares `a` and multiplies `res` by `a` when the least significant bit of `b` is 1. After the loop, it returns `res`, which is equivalent to \( a^b \mod 998244353 \). This process ensures that the intermediate values of `a` are always powers of 2 (i.e., \( a^{2^k} \)), where `k` is the number of iterations in the loop. The function handles the case where `b` is initially greater than 0 and reduces the problem size in each iteration until `b` becomes 0, at which point the final value of `res` is returned.

#State of the program right berfore the function call: a is an integer such that \(0 < a < 998244353\)
def func_3(a):
    return func_2(a, MOD - 2)
    #The program returns the value of `func_2(a, 998244351)` where `a` is an integer such that \(0 < a < 998244353\)
#Overall this is what the function does:The function `func_3` accepts an integer `a` such that \(0 < a < 998244353\) and returns the value of `func_2(a, 998244351)`. There are no additional actions performed by `func_3` beyond calling `func_2` with the specified arguments. The function does not modify any variables outside its scope and does not have any side effects. The return value is solely dependent on the input `a` and the constant `998244351`.

