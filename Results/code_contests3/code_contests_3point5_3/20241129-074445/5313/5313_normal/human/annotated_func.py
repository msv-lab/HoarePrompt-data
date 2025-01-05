#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 10^6.**
def func():
    n = int(input())
    x = int(n ** 0.5)
    if (x ** 2 == n) :
        answr = x * 4
    else :
        if (x * (x + 1) > n) :
            answr = (x + x + 1) * 2
        else :
            answr = 4 * (x + 1)
        #State of the program after the if-else block has been executed: *N is a positive integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the square root of n. If x * (x + 1) > n, then answr is calculated based on x. Otherwise, if x * (x + 1) ≤ n, then answr = 4 * (x + 1)
    #State of the program after the if-else block has been executed: *N is a positive integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the square root of n. If x^2 = n, then answr is 4 times the square root of n. Otherwise, if x * (x + 1) > n, then answr is calculated based on x. If x * (x + 1) ≤ n, then answr = 4 * (x + 1)
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` takes an integer input `n` and calculates the square root `x` of `n`. If the square of `x` is equal to `n`, it sets the answer `answr` to 4 times the square root of `n`. If `x` multiplied by `x + 1` is greater than `n`, it calculates `answr` based on `x`. Otherwise, if `x` multiplied by `x + 1` is less than or equal to `n`, it sets `answr` to 4 times `x + 1`. The function then prints the integer value of `answr`.

