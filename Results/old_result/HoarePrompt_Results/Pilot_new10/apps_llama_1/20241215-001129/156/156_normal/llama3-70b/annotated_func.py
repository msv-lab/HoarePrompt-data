#State of the program right berfore the function call: n and m are positive integers where n is even, and k is a non-negative integer such that 0 <= k < n*m.
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
        #State of the program after the if-else block has been executed: `n` and `m` are input integers, `k` is in the range 0 to 2n - 3, and `k` is greater than or equal to `n - 1`. If `k` is less than `n * 2 - 2`, two values are printed: the first is `n - (k - n + 1) % (n - 1) - 1` which ranges from 0 to `n - 1`, and the second is always 1. If `k` is greater than or equal to `n * 2 - 2`, the program prints 1 and 2.
    #State of the program after the if-else block has been executed: `n` and `m` are input integers, `k` is in the range 0 to 2n - 3. If `k` is less than `n - 1`, the values of `k + 1` and 1 have been printed. If `k` is greater than or equal to `n - 1` and less than `n * 2 - 2`, the values of `n - (k - n + 1) % (n - 1) - 1` and 1 have been printed. If `k` is greater than or equal to `n * 2 - 2`, the values of 1 and 2 have been printed.
#Overall this is what the function does:The function accepts three parameters `n`, `m`, and `k` as input from the user, where `n` and `m` are positive integers and `k` is a non-negative integer, then prints specific values based on the reduced range of `k` modulo `n * 2 - 2`, without handling cases where `n` is odd or `k` is out of range, and without returning any messages.

