#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 10^9 and n is an even integer; k is a non-negative integer such that 0 <= k < n·m.
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
        #State of the program after the if-else block has been executed: *`n` and `m` are integers, with `n` being an even integer between 2 and 10^9, and `k` updated to `k % (n * 2 - 2)`. If `k < n * 2 - 2`, output values are computed as `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. Otherwise, if `k` is greater than or equal to `n * 2 - 2`, then the output is 1 and 2.
    #State of the program after the if-else block has been executed: *`n` is an even integer assigned from input, `m` is an integer assigned from input, and `k` is updated to `k % (n * 2 - 2)` within the bounds `0 <= k < n · m` and `2 <= n, m <= 10^9`. If `k < n - 1`, the output values are `(k + 1, 1)`. Otherwise, if `k < n * 2 - 2`, the output values are computed as `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. If `k` is greater than or equal to `n * 2 - 2`, the output is 1 and 2.
#Overall this is what the function does:The function accepts two integers, `n` (an even integer between 2 and 10^9) and `m` (an integer within the same range), along with a non-negative integer `k` (0 <= k < n·m). It computes a modified value of `k` using modulo arithmetic (`k % (n * 2 - 2)`) and produces different outputs based on the resulting value of `k`. 

Specifically:
- If `k < n - 1`, it outputs the values `(k + 1, 1)`.
- If `n - 1 <= k < n * 2 - 2`, it calculates and outputs `(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)`.
- If `k >= n * 2 - 2`, it outputs `(1, 2)`.

The output consists of two integers and is determined entirely based on the value of `k`, which factors in a wrapping behavior due to the modulo operation. The constraints ensure that the function handles edge cases well, as long as inputs adhere to the specified ranges. The code does not account for invalid input (e.g., inputs outside defined bounds), but given the problem context, it's assumed that inputs will always be valid.

