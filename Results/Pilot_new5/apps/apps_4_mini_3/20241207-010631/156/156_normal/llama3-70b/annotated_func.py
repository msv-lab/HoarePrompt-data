#State of the program right berfore the function call: n and m are even integers in the range [2, 10^9], k is a non-negative integer such that 0 <= k < n * m.
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
        #State of the program after the if-else block has been executed: *`n` and `m` are even integers in the range [2, 10^9]. If `k` is less than `n * 2 - 2`, the output is (n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1). Otherwise, if `k` is greater than or equal to `n * 2 - 2`, then `k` is still updated to `k % (n * 2 - 2)` and maintains its value that is greater than or equal to `n - 1`.
    #State of the program after the if-else block has been executed: *`n` and `m` are even integers in the range [2, 10^9]. If `k` is less than `n - 1`, the output is (k + 1, 1). If `k` is less than `n * 2 - 2`, the output is (n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1). Otherwise, if `k` is greater than or equal to `n * 2 - 2`, then `k` is updated to `k % (n * 2 - 2)` and maintains its value that is greater than or equal to `n - 1.
#Overall this is what the function does:The function accepts three parameters: two even integers `n` and `m` (both in the range [2, 10^9]) and a non-negative integer `k` (where 0 <= k < n * m). It processes `k` to determine and print specific coordinates based on its value relative to `n`. If `k` is less than `n - 1`, it prints (k + 1, 1). If `k` is between `n - 1` and `n * 2 - 2`, it computes and prints the coordinates based on a calculation involving `n` and `k`. If `k` is greater than or equal to `n * 2 - 2`, it defaults to printing the coordinates (1, 2). The function does not return any value; it only prints the results.

