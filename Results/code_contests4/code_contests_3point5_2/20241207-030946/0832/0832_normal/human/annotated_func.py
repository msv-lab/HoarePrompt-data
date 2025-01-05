#State of the program right berfore the function call: n and m are even integers such that 2 ≤ n, m ≤ 10^9, and k is a non-negative integer less than n*m.**
def func():
    n, m, k = map(int, raw_input().split())
    x = 1
    y = 1
    if (k - n <= -1) :
        print(y, k + 1)
        sys.exit()
    #State of the program after the if block has been executed: *n and m are even integers such that 2 ≤ n, m ≤ 10^9, k is a non-negative integer less than n*m, x is 1, y is 1. If k - n <= -1, the program prints k + 1.
    k -= n
    t = k / (m - 1)
    p = k % (m - 1)
    y = n - t
    x = 2 + p if t % 2 == 0 else m - p
    print(int(math.ceil(y)), int(x))
    print(y, x)
#Overall this is what the function does:The function `func` reads input values for n, m, and k, where n and m are even integers between 2 and 10^9, and k is a non-negative integer less than n*m. It then calculates x and y based on the input values, and prints the result. If k - n is less than or equal to -1, it prints y and k + 1. The function does not explicitly return a value.

