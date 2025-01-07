#State of the program right berfore the function call: n and m are positive integers with n being even, k is a non-negative integer such that 0 <= k < n*m.
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
        #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is equal to `k % (2*n - 2)` and is greater than or equal to `n - 1`. If `k` is less than `n * 2 - 2`, then two values have been printed: the first is `n - (k - n + 1) % (n - 1) - 1`, which cycles through a range determined by `n`, and the second is `(k - n + 1) // (n - 1) + 1`, which is either 1 or 2. If `k` is greater than or equal to `n * 2 - 2`, then the values 1 and 2 have been printed.
    #State of the program after the if-else block has been executed: *`n` is an input integer, `m` is an input integer, `k` is the remainder of the division of the original `k` by `n * 2 - 2`. If `k` is less than `n - 1`, then `k + 1` and `1` have been printed. If `k` is greater than or equal to `n - 1` and less than `n * 2 - 2`, then `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1` have been printed. If `k` is greater than or equal to `n * 2 - 2`, then `1` and `2` have been printed.
#Overall this is what the function does:The function accepts three parameters, n, m, and k, from user input, where n and m are expected to be positive integers with n being even, and k is a non-negative integer. The function normalizes k to be within the range 0 to 2n - 3 by taking k modulo (2n - 2). It then prints two values based on the normalized value of k. If k is less than n - 1, it prints k + 1 and 1. If k is greater than or equal to n - 1 and less than n * 2 - 2, it prints two computed values that cycle through a range determined by n. If k is greater than or equal to n * 2 - 2, it prints 1 and 2, although this case is technically impossible due to the initial normalization of k. The function does not return any value, as it's designed to print output directly. After execution, the program state reflects the input values of n, m, and the normalized k, with the printed values being the primary outcome. The function does not explicitly validate the input conditions (n being even, k being within the specified range before normalization), but it will operate based on the provided inputs, potentially leading to unexpected behavior if these conditions are not met.

