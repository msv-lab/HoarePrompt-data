#State of the program right berfore the function call: n is a positive integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    if (n == 2) :
        print('NO')
    else :
        print('YES')
        k = 2
        print(k)
        print('1', n // 2)
        print('1', n)
    #State of the program after the if-else block has been executed: *`n` is an integer within the range of 2 to \(10^9\), inclusive. If `n` equals 2, the console outputs 'NO'. Otherwise, the console outputs 'YES', `k` is set to 2, and the values '1' and `n // 2' are printed. If `n` does not equal 2, the values '1' and `n` are printed to the console.
#Overall this is what the function does:The function `func()` takes no parameters and processes a positive integer `n` where \(2 \leq n \leq 10^9\). If `n` is 2, it prints 'NO'. Otherwise, it prints 'YES', sets `k` to 2, and prints `k`, followed by '1' and `n // 2`. If `n` is not 2, it prints 'YES', sets `k` to 2, and prints `k`, followed by '1' and `n`. This covers all possible values of `n` within the specified range.

