#State of the program right berfore the function call: base is a non-negative integer, exponent is a non-negative integer, and mod is a positive integer (10^9 + 7).
def func_1(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base % mod
        
        base = base * base % mod
        
        exponent //= 2
        
    #State of the program after the loop has been executed: base: base^(original_exponent // 2^k) % mod, exponent: 0, result: base raised to the power of the sum of the odd parts of original exponent modulo mod.
    return result
    #The program returns base raised to the power of the sum of the odd parts of original exponent modulo mod
#Overall this is what the function does:The function `func_1` accepts three parameters: `base`, `exponent`, and `mod`. `base` is a non-negative integer, `exponent` is a non-negative integer, and `mod` is a positive integer (10^9 + 7). The function calculates `base` raised to the power of the sum of the odd parts of the original `exponent` modulo `mod`. This is achieved through a loop where the `exponent` is repeatedly halved, and the `base` is squared, reducing the problem size efficiently. If the current `exponent` is odd, the `base` is multiplied by the current `result` and then taken modulo `mod`. The loop continues until the `exponent` becomes zero. The function returns the final `result` which is `base` raised to the power of the sum of the odd parts of the original `exponent` modulo `mod`.

#State of the program right berfore the function call: x is a non-negative integer representing the initial number of dresses, k is a non-negative integer representing the number of months in a year minus one (k + 1 is the total number of months in the year), and MOD is a constant equal to 10^9 + 7.
def func_2(x, k):
    if (x == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: x is a non-negative integer representing the initial number of dresses, k is a non-negative integer representing the number of months in a year minus one (k + 1 is the total number of months in the year), and MOD is a constant equal to 10^9 + 7. x is not equal to 0.
    power = func_1(2, k + 1, MOD)

result = x * (power - 1) % MOD % MOD
    return result
    #`The program returns the value of x * (2^(k+1) - 1) mod (10^9 + 7)`
#Overall this is what the function does:The function `func_2` accepts two parameters: `x` (a non-negative integer representing the initial number of dresses) and `k` (a non-negative integer representing the number of months in a year minus one, with `k + 1` being the total number of months in the year). It uses another function `func_1` to compute `2^(k+1)` modulo `10^9 + 7`. If `x` is 0, the function returns 0. Otherwise, it calculates `x * (2^(k+1) - 1) % (10^9 + 7)` and returns this value. The function ensures that all intermediate and final results are taken modulo `10^9 + 7` to prevent overflow.

