#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
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
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 <= n <= 10^9. If `n` equals 2, the value of `n` remains unchanged. If `n` is not 2, then `n` is an integer such that 1 <= n <= 5 × 10^8, `k` is 2, and the program has printed '1' followed by the value of `n // 2`
#Overall this is what the function does:The function accepts an integer `n` (where `2 <= n <= 10^9`) and prints 'NO' if `n` is 2. If `n` is not 2, it prints 'YES', sets `k` to 2, and prints `k`, followed by '1' and `n // 2`, and finally '1' and `n`.

