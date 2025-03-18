#State of the program right berfore the function call: The function should accept two parameters, n and k, where n is the number of coins Alice has and k is the number of jewels Bob wants Alice to buy, both are positive integers such that 1 ≤ n, k ≤ 10^18. The function should also handle multiple test cases, indicated by an integer t where 1 ≤ t ≤ 1000.
def func_1():
    n, k = map(int, input().split())
    if (n < k) :
        print('NO')
        #This is printed: NO
    else :
        if (n == k) :
            print('YES')
            #This is printed: YES
            print(1)
            #This is printed: 1
            print(n)
            #This is printed: n (where n is the value of n, which is equal to k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1, 1 (where n - k + 1 is a positive integer calculated as n - k + 1 and 1 is the explicit value)
            else :
                print('NO')
                #This is printed: NO
            #State: `n` and `k` are positive integers such that 1 ≤ `n`, `k` ≤ 10^18, and `t` is an integer where 1 ≤ `t` ≤ 1000. `n` and `k` are assigned values from the input, and `n` is greater than or equal to `k`, with `n` not equal to `k`. If `k - 1 < n - k + 1`, then `k` is less than `n - k + 2`. Otherwise, `k - 1 >= n - k + 1`.
        #State: `n` and `k` are positive integers such that 1 ≤ `n`, `k` ≤ 10^18, and `t` is an integer where 1 ≤ `t` ≤ 1000. `n` and `k` are assigned values from the input, and `n` is greater than or equal to `k`. If `n` is equal to `k`, no further changes are made. If `n` is not equal to `k`, then either `k - 1 < n - k + 1` (implying `k` is less than `n - k + 2`), or `k - 1 >= n - k + 1`.
    #State: *`n` and `k` are positive integers such that 1 ≤ `n`, `k` ≤ 10^18, and `t` is an integer where 1 ≤ `t` ≤ 1000. If `n` < `k`, no further changes are made to `n` and `k`. If `n` ≥ `k`, and `n` is equal to `k`, no further changes are made. If `n` > `k`, then either `k - 1 < n - k + 1` (implying `k` is less than `n - k + 2`), or `k - 1 ≥ n - k + 1`.
#Overall this is what the function does:The function `func_1` processes a series of test cases, each defined by two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), where `n` represents the number of coins Alice has and `k` represents the number of jewels Bob wants Alice to buy. For each test case, the function checks if Alice has enough coins to buy the jewels. If `n` is less than `k`, the function prints "NO". If `n` is equal to `k`, the function prints "YES", followed by "1" and the value of `n`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, the function prints "YES", followed by "2" and the values `n - k + 1` and `1`. Otherwise, if `n` is greater than `k` and `k - 1` is greater than or equal to `n - k + 1`, the function prints "NO". The function does not return any values; it only prints the results to the console.

