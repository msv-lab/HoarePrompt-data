#State of the program right berfore the function call: Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^{18}) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. There are t (1 ≤ t ≤ 1000) such test cases.
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
            #This is printed: n (where n is the value of n, and n is equal to k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1, 1 (where n - k + 1 is a positive integer greater than 1)
            else :
                print('NO')
                #This is printed: NO
            #State: `n` and `k` are the two positive integers read from the input for the current test case, and there are `t` such test cases. `n` is greater than or equal to `k`, and `n` is not equal to `k`. Additionally, if `k - 1 < n - k + 1`, then `k - 1` is less than `n - k + 1`; otherwise, `k - 1` is not less than `n - k + 1`.
        #State: `n` and `k` are the two positive integers read from the input for the current test case, and there are `t` such test cases. `n` is greater than or equal to `k`. If `n` is equal to `k`, no additional changes are made. Otherwise, `n` is greater than `k`, and `k - 1` is either less than `n - k + 1` or not less than `n - k + 1`.
    #State: `n` and `k` are the two positive integers read from the input for the current test case, and there are `t` such test cases. If `n` is less than `k`, no additional changes are made. If `n` is greater than or equal to `k`, and `n` is equal to `k`, no additional changes are made. Otherwise, `n` is greater than `k`, and `k - 1` is either less than `n - k + 1` or not less than `n - k + 1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two positive integers `n` and `k`. For each test case, it determines if Alice can buy exactly `k` jewels with her `n` coins and prints "YES" or "NO" accordingly. If `n` is equal to `k`, it also prints the number of purchases (1) and the number of coins used (`n`). If `n` is greater than `k` and a specific condition is met (`k - 1 < n - k + 1`), it prints the number of purchases (2) and the distribution of coins used (`n - k + 1` and `1`).

