#State of the program right berfore the function call: N is an integer such that 2 ≦ N ≦ 10^{12}, and X is an integer such that 1 ≦ X ≦ N-1.
def func():
    L = map(int, raw_input().split())
    n = L[0]
    x = L[1]
    res = n
    a = x
    b = n - x
    flag = True
    while flag:
        if a > b:
            q = a // b
            a -= q * b
            res += 2 * q * b
        elif b > a:
            q = b // a
            b -= q * a
            res += 2 * a * q
        else:
            res += a
            flag = False
        
    #State of the program after the loop has been executed: Output State: `a` and `b` are equal, representing the GCD of `x` and `n - x`, `res` is equal to `n + 2 * GCD * k`, where `k` is the number of subtractions performed, and `flag` is `False`.
    print(res)
#Overall this is what the function does:The function `func` accepts two parameters, `N` and `X`, where `N` is an integer between 2 and \(10^{12}\), and `X` is an integer between 1 and \(N-1\). The function calculates the greatest common divisor (GCD) of `X` and `N - X` using the Euclidean algorithm and updates the result (`res`) accordingly. The function then prints the final value of `res`, which is `N + 2 * GCD * k`, where `k` is the number of subtractions performed during the process. The function does not return anything explicitly; instead, it relies on printing the result directly. Potential edge cases include when `N` is at its minimum value (2) and `X` is 1, or when `X` is close to `N`. The function does not handle these cases specifically within the provided code.

