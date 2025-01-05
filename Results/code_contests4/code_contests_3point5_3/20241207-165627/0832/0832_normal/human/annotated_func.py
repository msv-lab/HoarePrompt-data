#State of the program right berfore the function call: n and m are even integers greater than or equal to 2, and k is a non-negative integer less than n*m.**
def func():
    n, m, k = map(int, raw_input().split())
    x = 1
    y = 1
    if (k - n <= -1) :
        print(y, k + 1)
        sys.exit()
    #State of the program after the if block has been executed: *`n` and `m` are even integers greater than or equal to 2, `k` is a non-negative integer less than `n*m`, `x` is 1, `y` is 1. If `k - n <= -1`, the code prints the value of `y` (which is 1) and `k + 1`, where `k` is a non-negative integer less than `n*m`.
    k -= n
    t = k / (m - 1)
    p = k % (m - 1)
    y = n - t
    x = 2 + p if t % 2 == 0 else m - p
    print(int(math.ceil(y)), int(x))
    print(y, x)
#Overall this is what the function does:The function `func` reads input for integers n, m, and k. It then calculates values for x and y based on specific conditions. If k - n is less than or equal to -1, it prints y and k + 1 and exits the program. Otherwise, it updates the values of k, t, p, y, and x accordingly, and prints the calculated values of y and x. The function does not return any value but operates on the predefined parameters n, m, and k.

