#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If `a + b` is greater than or equal to `mod`, then `c` is subtracted by `mod`. Otherwise, there is no change in the values of `a`, `b`, `c`.
    return c
    #The program returns the value of 'c' after checking if 'a + b' is greater than or equal to 'mod' and subtracting 'mod' from 'c' if the condition is met.
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b, calculates the sum of a and b in variable c, and returns the value of c. If the sum of a and b is greater than or equal to the variable mod, it subtracts mod from c before returning it. If the sum of a and b is less than mod, c remains unchanged.

#State of the program right berfore the function call: **
def func_2(a, b):
    return (a - b) % mod
    #The program returns the result of subtracting variable 'b' from variable 'a' and then taking the modulo 'mod' of the result
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b` and returns the result of subtracting `b` from `a` and then taking the modulo 'mod' of the result. The function does not handle the case where `mod` is not defined or initialized, which could lead to an error.

#State of the program right berfore the function call: N and K are positive integers such that 1 <= K <= N. A_i are integers such that |A_i| <= 10^9.**
def func_3(a, b):
    return a * b % mod
    #The program returns the result of the product of integers a and b modulo mod. The variables a and b are positive integers, and mod is a positive integer.
#Overall this is what the function does:The function accepts two positive integers a and b, along with a positive integer mod, and returns the result of the product of a and b modulo mod. The code accurately calculates the product of a and b modulo mod. However, a potential edge case to consider is if the product of a and b exceeds the maximum value that can be represented by the data type used, which could lead to an overflow issue. This aspect is not addressed in the annotations.

#State of the program right berfore the function call: N and K are positive integers such that 1 <= K <= N. A_i are integers such that |A_i| <= 10^9.**
def func_4(a, b):
    if (b == 0) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: *N and K are positive integers such that 1 <= K <= N. A_i are integers such that |A_i| <= 10^9. b is not equal to 0
    if (b % 2 == 1) :
        return func_3(a, func_4(a, b - 1))
        #The program returns the result of calling function func_3 with parameters a and the result of calling function func_4 with parameters a and b-1
    else :
        temp = func_4(a, b / 2)
        return temp * temp
        #The program returns the square of the value returned by func_4(a, b / 2)
#Overall this is what the function does:The function `func_4` accepts two positive integers `a` and `b` where 1 <= b <= a. It has three return cases:
1. If `b` is equal to 0, the function returns 1.
2. If `b` is odd, the function recursively calls `func_3` with parameters `a` and the result of `func_4` with parameters `a` and `b-1`.
3. If `b` is even, the function recursively calculates the square of the value returned by calling itself with parameters `a` and `b/2`.
Therefore, the functionality of the function is to perform recursive calculations based on the parity of `b` and return different values accordingly.

#State of the program right berfore the function call: **
def func_5(a):
    return func_4(a, mod - 2)
    #The program returns the result of calling the function func_4 with parameters 'a' and 'mod - 2'
#Overall this is what the function does:The function `func_5` accepts a parameter `a` and returns the result of calling the function `func_4` with parameters 'a' and 'mod - 2'. The functionality does not provide details on the behavior of `func_4` or the value of `mod`. It assumes that `func_4` exists with the specified parameters.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n, and |A_i| <= 10^9 for each element A_i in the list.**
def func_6(n, k, fac):
    if (k > n) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *n and k are positive integers such that 1 <= k <= n, and |A_i| <= 10^9 for each element A_i in the list. k is less than or equal to n
    return func_3(fac[n], func_5(func_3(fac[n - k], fac[k])))
    #The program returns the result of calling function func_3 with fac[n] as the first argument and the result of calling function func_5 with the result of calling function func_3 with fac[n-k] and fac[k] as arguments
#Overall this is what the function does:The function `func_6` accepts three parameters `n`, `k`, and `fac`. It then checks if `k` is greater than `n` and returns 0 in that case. Otherwise, it returns the result of nested function calls involving values from the list `fac`. The functionality is dependent on the relation between `n` and `k`, and the values stored in `fac`.

#State of the program right berfore the function call: N and K are positive integers such that 1 <= K <= N. A_i are integers such that |A_i| <= 10^9.**
def func_7():
    n, k = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    fac = [0] * (n + 5)
    fac[0] = 1
    for i in range(1, n + 5):
        fac[i] = func_3(fac[i - 1], i)
        
    #State of the program after the  for loop has been executed: fac contains the values calculated by func_3 for each index i, with fac[0] = 1 and fac[1] to fac[n+4] updated accordingly
    a.sort()
    ans = 0
    for i in range(n - 1):
        diff = func_2(a[i + 1], a[i])
        
        ways = func_6(n, k, fac)
        
        ways = func_2(ways, func_6(i + 1, k, fac))
        
        ways = func_2(ways, func_6(n - i - 1, k, fac))
        
        ans = func_1(ans, func_3(diff, ways))
        
    #State of the program after the  for loop has been executed: `fac` contains values calculated by `func_3` for each index `i` starting from `fac[0] = 1` up to `fac[n+4]`, `a` is sorted in ascending order, `ans` is updated by applying `func_1` on the previous value of `ans`, `func_3(diff, ways)`, `n` is at least 2, `diff` is assigned the result of `func_2(a[n-1], a[n-2])`, and `ways` is the result of `func_2(ways, func_6(n, k, fac))`
    print(ans)
#Overall this is what the function does:The function `func_7` reads input values `n`, `k`, and a list `a`, calculates factorial values using `func_3`, sorts the list `a`, and performs various calculations on `a` elements based on `n`, `k`, and factorial values. After the computations, it prints the final result `ans`. The function does not accept any parameters and does not return any value.

