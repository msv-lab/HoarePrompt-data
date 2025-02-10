#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n and k are positive integers where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively.
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
            print(1)
            #This is printed: 1
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: (n - k + 1, 1) (where n - k + 1 is the result of the expression n - k + 1 and 1 is the constant integer value)
            else :
                print('NO')
                #This is printed: NO
            #State: `t` is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. `n` and `k` are specific positive integers read from the input, where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively. Additionally, `n` is greater than or equal to `k`, and `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, the condition `(k - 1 < n - k + 1)` is true. Otherwise, `k - 1` is greater than or equal to `n - k + 1`.
        #State: `t` is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. `n` and `k` are specific positive integers read from the input, where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively. Additionally, `n` is greater than or equal to `k`. If `n` is equal to `k`, the condition holds as is. Otherwise, if `k - 1` is less than `n - k + 1`, the condition `(k - 1 < n - k + 1)` is true. If `k - 1` is greater than or equal to `n - k + 1`, the condition `(k - 1 >= n - k + 1)` is true.
    #State: *`t` is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. `n` and `k` are specific positive integers read from the input, where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively. If `n` is less than `k`, the condition holds as is. Otherwise, if `n` is greater than or equal to `k`, the condition holds as is. Additionally, if `n` is greater than or equal to `k`, and `k - 1` is less than `n - k + 1`, the condition `(k - 1 < n - k + 1)` is true. If `k - 1` is greater than or equal to `n - k + 1`, the condition `(k - 1 >= n - k + 1)` is true.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `n` represents the number of coins Alice has and `k` represents the number of jewels Bob wants Alice to buy. It then checks the relationship between `n` and `k` and prints one of the following outputs based on the conditions:
- If `n` is less than `k`, it prints "NO".
- If `n` is equal to `k`, it prints "YES" followed by two lines, each containing the number 1.
- If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES", followed by the number 2, and then the values `n - k + 1` and 1 on the next line.
- If `n` is greater than `k` and `k - 1` is greater than or equal to `n - k + 1`, it prints "NO".

