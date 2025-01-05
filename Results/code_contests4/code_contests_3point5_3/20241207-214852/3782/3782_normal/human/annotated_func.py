#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`c` is a value greater than or equal to `mod`. When `c` is greater than or equal to `mod`, the program does not change the values of any variables.
    return c
    #The program returns the value of 'c', which is greater than or equal to 'mod'.
#Overall this is what the function does:The function func_1 accepts two parameters `a` and `b`, calculates the sum of `a` and `b` in variable `c`, and then checks if `c` is greater than or equal to `mod`. If `c` is greater than or equal to `mod`, it subtracts `mod` from `c`. The function then returns the value of `c`, which is guaranteed to be greater than or equal to `mod`.

#State of the program right berfore the function call: **
def func_2(a, b):
    return (a - b) % mod
    #The program returns the result of subtracting variable 'b' from variable 'a' and then taking the modulus 'mod' of the result
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b`, subtracts `b` from `a`, and returns the result modulo `mod`. The function does not handle any edge cases such as division by zero or non-integer inputs. It simply performs the subtraction and modulus operation as described in the code.

#State of the program right berfore the function call: **
def func_3(a, b):
    return a * b % mod
    #The program returns the result of the product of 'a' and 'b' modulo 'mod'
#Overall this is what the function does:The function `func_3` accepts two integer parameters `a` and `b`, and returns the result of the product of 'a' and 'b' modulo 'mod'.

#State of the program right berfore the function call: **N and K are positive integers such that 1 <= K <= N. A_i are integers where 1 <= i <= N and |A_i| <= 10^9.
def func_4(a, b):
    if (b == 0) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: *N and K are positive integers such that 1 <= K <= N. A_i are integers where 1 <= i <= N and |A_i| <= 10^9. b is not equal to 0
    if (b % 2 == 1) :
        return func_3(a, func_4(a, b - 1))
        #The program returns the result of calling function func_3 with parameters a and the result of calling function func_4 with parameters a and (b-1)
    else :
        temp = func_4(a, b / 2)
        return temp * temp
        #The program returns the result of calling `func_4(a, b / 2)` squared
#Overall this is what the function does:The function `func_4` takes two positive integer parameters `a` and `b` where 1 <= K <= N. It has three cases:
Case 1: If `b` is 0, the function returns 1.
Case 2: If `b` is odd, it returns the result of calling function `func_3` with parameters `a` and the result of calling function `func_4` with parameters `a` and `(b-1)`.
Case 3: If `b` is even, it returns the squared result of calling `func_4(a, b / 2)`.
Therefore, the functionality of the function is to perform recursive calculations based on the parity of `b` and return the corresponding results.

#State of the program right berfore the function call: N and K are positive integers such that 1 <= K <= N, and A_i are integers such that |A_i| <= 10^9.**
def func_5(a):
    return func_4(a, mod - 2)
    #The program returns the result of calling func_4(a, mod - 2)
#Overall this is what the function does:The function `func_5` accepts a list of integers `a` as a parameter. It then calls another function `func_4` with the input `a` and `mod - 2`, where `mod` seems to be a global variable representing a modulus value. The function `func_5` essentially acts as a wrapper function that modifies the input `a` before passing it to `func_4`. The constraints on the input parameters ensure that `a` contains integers with absolute values less than or equal to 10^9.

#State of the program right berfore the function call: **
def func_6(n, k, fac):
    if (k > n) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: `k`, `n` are integers. `k` is less than or equal to `n`
    return func_3(fac[n], func_5(func_3(fac[n - k], fac[k])))
    #The program returns the result of func_3(fac[n]) multiplied by the result of func_5(func_3(fac[n - k], fac[k]))
#Overall this is what the function does:The function `func_6` accepts three parameters: `n`, `k`, and `fac`. It then checks if `k` is greater than `n` and returns 0 in that case. Otherwise, it calculates the result of `func_3(fac[n])` multiplied by the result of `func_5(func_3(fac[n - k], fac[k]))`.

#State of the program right berfore the function call: N and K are positive integers such that 1 <= K <= N. A_i are integers such that |A_i| <= 10^9.**
def func_7():
    n, k = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    fac = [0] * (n + 5)
    fac[0] = 1
    for i in range(1, n + 5):
        fac[i] = func_3(fac[i - 1], i)
        
    #State of the program after the  for loop has been executed: fac contains the result of applying func_3 iteratively on fac[0] to fac[n+4]
    a.sort()
    ans = 0
    for i in range(n - 1):
        diff = func_2(a[i + 1], a[i])
        
        ways = func_6(n, k, fac)
        
        ways = func_2(ways, func_6(i + 1, k, fac))
        
        ways = func_2(ways, func_6(n - i - 1, k, fac))
        
        ans = func_1(ans, func_3(diff, ways))
        
    #State of the program after the  for loop has been executed: `fac` contains the result of applying `func_3` iteratively on `fac[0]` to `fac[n+4]`, `a` is sorted, `ans` is the final result after applying `func_1` iteratively on the results of `func_3(diff, ways)` for all iterations of the loop, `i` is `n - 1`, `diff` is the result of `func_2(a[i + 1], a[i])` for the last iteration, `ways` is the final result after applying all `func_2` and `func_6` functions iteratively for all iterations of the loop
    print(ans)
#Overall this is what the function does:The function `func_7` reads input integers N and K, and a list of integers A. It then calculates various values using helper functions `func_2`, `func_3`, and `func_6`, and eventually prints the final result `ans`. The function does not explicitly return a value. However, the annotations indicate the postconditions based on the calculations performed, but it is essential to note that the actual functionality may deviate from the annotations due to potential missing logic or edge cases in the code.

