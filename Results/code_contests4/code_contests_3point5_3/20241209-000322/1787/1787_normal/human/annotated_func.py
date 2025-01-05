#State of the program right berfore the function call: **
def func_1():
    fact = [1]
    for i in range(1, 100005):
        fact.append(fact[-1] * i % mod)
        
    #State of the program after the  for loop has been executed: `fact` is a list containing the factorial values modulo `mod` for `i` ranging from 1 to 100004, `i` is 100004, `mod` is the divisor used in the modulo operation
    ifact = [0] * 100005
    ifact[100004] = pow(fact[100004], mod - 2, mod)
    for i in range(100004, 0, -1):
        ifact[i - 1] = i * ifact[i] % mod
        
    #State of the program after the  for loop has been executed: `fact` is a list containing the factorial values modulo `mod` for `i` ranging from 1 to 100004, `i` is 0, `mod` is the divisor used in the modulo operation; `ifact` is a list of calculated modular inverses for `i` ranging from 0 to 100004
    return fact, ifact
    #The program returns the list `fact` containing factorial values modulo `mod` for `i` ranging from 1 to 100004, and the list `ifact` containing calculated modular inverses for `i` ranging from 0 to 100004
#Overall this is what the function does:The function func_1 calculates and stores factorial values modulo `mod` for `i` ranging from 1 to 100004 in the list `fact`, and calculates and stores modular inverses for `i` ranging from 0 to 100004 in the list `ifact`. The function does not accept any parameters and returns the lists `fact` and `ifact`.

#State of the program right berfore the function call: **
def func_2(n, p):
    return pow(n, p - 2, p)
    #The program returns the value of n raised to the power of p minus 2, modulo p.
#Overall this is what the function does:The function `func_2` accepts two integer parameters, `n` and `p`, and returns the value of `n` raised to the power of `p` minus 2, modulo `p`. The function performs modular exponentiation with an exponent of `p - 2`.

#State of the program right berfore the function call: **
def func_3(n, r, fact, ifact):
    t = fact[n] * (ifact[r] * ifact[n - r]) % mod % mod
    return t
    #The program returns the value of 't' which is calculated based on the unknown values of 'n', 'r', 'fact', 'ifact', and 'mod'
#Overall this is what the function does:The function `func_3` accepts four parameters: `n`, `r`, `fact`, and `ifact`, along with an assumed parameter `mod`. It calculates the value of `t` based on these parameters and returns it. The specific calculation method is not provided in the annotations, but the function is designed to perform some computation using the given parameters and return the result as `t`. The actual calculation logic is not explicitly stated, so the exact functionality may vary depending on the implementation.

#State of the program right berfore the function call: **
def func_4():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers after converting the input read from the standard input using sys.stdin.readline().strip().split()
#Overall this is what the function does:The function `func_4` reads input from the standard input, converts it to integers, and returns a map object containing these integers. It does not accept any parameters.

#State of the program right berfore the function call: **
def func_5():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers after converting input from standard input using the map function
#Overall this is what the function does:The function `func_5` reads input from the standard input, splits it by spaces, converts each element to an integer, and returns a list of those integers.

#State of the program right berfore the function call: **Precondition**: **t is a positive integer representing the number of test cases. Each test case consists of an integer n (1 ≤ n ≤ 2 ⋅ 10^5) representing the length of the password, followed by n positive integers a_{1},a_{2},...,a_{n} (1 ≤ a_{i} ≤ 10^9) representing the initial contents of the password.**
def func_6():
    return sys.stdin.readline().strip()
    #The program returns the input from the standard input after stripping any leading or trailing whitespaces
#Overall this is what the function does:The function reads input from the standard input and returns it after stripping any leading or trailing whitespaces. The function does not explicitly mention handling the case when no input is provided or when the input is empty.

#State of the program right berfore the function call: **
def func_7(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the greatest common divisor of the original `x` and `y`, `y` is 0
    return x
    #The program returns the greatest common divisor of the original 'x' and 0, which is 'x' itself.
#Overall this is what the function does:The function `func_7` accepts two parameters `x` and `y`, calculates the greatest common divisor of the original `x` and `y`, and returns `x`, which is the greatest common divisor when `y` is 0. The function uses the Euclidean algorithm to find the greatest common divisor.

#State of the program right berfore the function call: **
def func_8(x, y):
    return x * y // func_7(x, y)
    #The program returns the result of multiplying variables x and y, then dividing the result by the return value of the function func_7 with arguments x and y.
#Overall this is what the function does:The function func_8 accepts two variables x and y, multiplies them, divides the result by the return value of the function func_7 with arguments x and y, and returns the final result.

#State of the program right berfore the function call: n is a positive integer representing the length of the password, and a is a list of n positive integers representing the initial contents of the password.**
def func_9(n):
    return [n, 1, n + 1, 0][n % 4]
    #The program returns one of the following values based on the value of n:
    #- If n is divisible by 4, the program returns n
    #- If n leaves a remainder of 1 when divided by 4, the program returns 1
    #- If n leaves a remainder of 2 when divided by 4, the program returns n+1
    #- If n leaves a remainder of 3 when divided by 4, the program returns 0
#Overall this is what the function does:The function `func_9` accepts a positive integer `n` representing the length of a password and returns a value based on the remainder of `n` when divided by 4. Specifically:
- If `n` is divisible by 4, the function returns `n`.
- If `n` leaves a remainder of 1 when divided by 4, the function returns 1.
- If `n` leaves a remainder of 2 when divided by 4, the function returns `n + 1`.
- If `n` leaves a remainder of 3 when divided by 4, the function returns 0.
The code accurately implements these conditions based on the value of `n`.

#State of the program right berfore the function call: **
def func_10(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a
            res %= MOD
            b -= 1
        else:
            a = a * a
            a %= MOD
            b >>= 1
        
    #State of the program after the loop has been executed: `res`, `a`, and `b` are integers. If `b` is True, then `res` is the result of `a` raised to the power of the original value of `b`, `a` is updated to the remainder of `a` divided by `MOD`. If `b` is False, then `res` remains the same as the initial value of 1, `a` is the result of `a` raised to the power of the original value of `b` if `b` was True, and `b` is False.
    res %= MOD
    return res
    #The program returns the remainder of 'res' divided by 'MOD'. The values of 'a' and 'b' remain the same as the initial state.
#Overall this is what the function does:The function `func_10` accepts two parameters `a` and `b` and calculates the remainder of `a` raised to the power of `b` divided by `MOD`. It updates the value of `a` and `b` during the process. The function then returns the final result after taking the remainder. If `b` is 0, the function will return 1 as the result.

#State of the program right berfore the function call: **
def func_11(P):
    ans = (-1 + sqrt(1 + 8 * P)) // 2
    return ans
    #The program returns the value of 'ans' which is calculated based on the unknown value of 'P'
#Overall this is what the function does:The function `func_11` accepts a parameter `P`, calculates the value of a variable `ans` using a mathematical formula involving `P`, and returns this calculated value. The function does not handle potential errors like division by zero or negative values of `P`, which could lead to incorrect results or exceptions. It solely focuses on calculating `ans` based on the provided `P`.

#State of the program right berfore the function call: **
def func_12():
    T = int(func_6())
    while T:
        n = int(func_6())
        
        Arr = func_5()
        
        p = Arr[0]
        
        flag = 0
        
        for i in Arr[1:]:
            if i != p:
                flag = 1
                break
        
        if flag == 1:
            print(1)
        else:
            print(n)
        
        T -= 1
        
    #State of the program after the loop has been executed: After the loop has executed, `T` is 0, `n`, `Arr`, `p`, `i`, and `flag` are non-zero integers. If any element in `Arr` after the first element is not equal to `p`, `flag` is set to 1. Otherwise, `flag` remains 0 after all iterations. If flag is equal to 1, then the flag remains 1. If flag is not equal to 1, it indicates that all elements in `Arr` after the first element are equal to `p` and `n` is printed.
#Overall this is what the function does:The function `func_12` does not accept any parameters and executes a loop controlled by the value of `T`. Within the loop, it initializes `n` by calling `func_6()` and creates a list `Arr` by calling `func_5()`. It then checks if all elements in `Arr` after the first element are equal to the first element `p`. If any element is different, it sets `flag` to 1; otherwise, `flag` remains 0. If `flag` is 1, it prints 1; otherwise, it prints `n`. The function iterates until `T` becomes 0. The function does not return any value.

