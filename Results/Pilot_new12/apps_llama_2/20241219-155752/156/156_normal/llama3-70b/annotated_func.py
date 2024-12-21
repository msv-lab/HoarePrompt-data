#State of the program right berfore the function call: n and m are positive even and positive integers respectively, such that 2 <= n and 2 <= m, and k is a non-negative integer such that 0 <= k < n * m.
def func():
    n, m, k = map(int, input().split())
    k %= n * 2 - 2
    if (k < n - 1) :
        print(k + 1, 1)
    else :
        if (k < n * 2 - 2) :
            print(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)
        else :
            print(1, 2)
        #State of the program after the if-else block has been executed: *`n` is a positive integer greater than or equal to 1, `m` is a positive integer greater than or equal to 1, `k` is a positive integer greater than or equal to `n - 1`. If `k` is less than `n * 2 - 2`, the printed values are `2n - k - 2` and `1`. If `k` is greater than or equal to `n * 2 - 2`, the values `1` and `2` have been printed to the console and `None` has been returned.
    #State of the program after the if-else block has been executed: `n` is a positive integer greater than or equal to 1, `m` is a positive integer greater than or equal to 1, `k` is a positive integer less than `n * 2 - 2`. If `k` is less than `n - 1`, `k + 1` and `1` have been printed. If `k` is greater than or equal to `n - 1` but less than `n * 2 - 2`, `2n - k - 2` and `1` have been printed. If `k` is greater than or equal to `n * 2 - 2`, `1` and `2` have been printed to the console and `None` has been returned.
#Overall this is what the function does:The function accepts three integer parameters `n`, `m`, and `k` as input from the user, where `n` and `m` are positive integers greater than or equal to 2, and `k` is a non-negative integer. It then calculates and prints a pair of values based on the input `n` and `k`, after applying the modulo operation `k %= n * 2 - 2`. If `k` is less than `n - 1`, it prints `k + 1` and `1`. If `k` is greater than or equal to `n - 1` but less than `n * 2 - 2`, it prints `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. If `k` is greater than or equal to `n * 2 - 2`, it prints `1` and `2`. The function does not explicitly return any value (i.e., it implicitly returns `None`), and the input `m` is not used in the calculation. After execution, the function's state includes the printed pair of values and the modified input `k` value, while the original input values `n`, `m`, and `k` are still present in the program's state.

