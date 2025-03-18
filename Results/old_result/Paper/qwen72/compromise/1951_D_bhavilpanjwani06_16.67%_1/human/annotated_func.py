#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 1000), and cases is a list of tuples where each tuple contains two positive integers n and k (1 ≤ n, k ≤ 10^18).
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
            #This is printed: - The `print(n)` statement will print the value of `n`, which is a positive integer equal to `k`.
            #
            #Output:
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: - The first value printed is `n - k + 1`.
                #   - The second value printed is `1`.
                #
                #Given the initial state and the conditions, the print statement will output the value of `n - k + 1` and `1`.
                #
                #Output:
            else :
                print('NO')
                #This is printed: NO
            #State: *`t` is a positive integer (1 ≤ t ≤ 1000), `cases` is a list of tuples where each tuple contains two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), `n` and `k` are the input integers, and `n` is greater than or equal to `k`. Additionally, `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, the current value of `k` satisfies this condition. Otherwise, `k - 1` is greater than or equal to `n - k + 1`.
        #State: *`t` is a positive integer (1 ≤ t ≤ 1000), `cases` is a list of tuples where each tuple contains two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), `n` and `k` are the input integers, and `n` is greater than or equal to `k`. If `n` is equal to `k`, the current tuple satisfies this condition. Otherwise, if `k - 1` is less than `n - k + 1`, the current value of `k` satisfies this condition. If `k - 1` is greater than or equal to `n - k + 1`, the current value of `k` does not satisfy the condition.
    #State: *`t` is a positive integer (1 ≤ t ≤ 1000), `cases` is a list of tuples where each tuple contains two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), `n` and `k` are the input integers. If `n` < `k`, the current value of `n` is less than the current value of `k`. If `n` ≥ `k`, the current value of `n` is greater than or equal to the current value of `k`. If `n` = `k`, the current tuple satisfies this condition. Otherwise, if `k - 1` < `n - k + 1`, the current value of `k` satisfies this condition. If `k - 1` ≥ `n - k + 1`, the current value of `k` does not satisfy the condition.
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from the user input. It then checks the relationship between `n` and `k` and prints one of the following outputs based on the conditions:
- If `n` is less than `k`, it prints 'NO'.
- If `n` is equal to `k`, it prints 'YES', followed by `1` and the value of `n`.
- If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints 'YES', followed by `2`, and then the values `n - k + 1` and `1`.
- If `n` is greater than `k` and `k - 1` is greater than or equal to `n - k + 1`, it prints 'NO'. 

The function does not return any value; it only prints the results to the console.

