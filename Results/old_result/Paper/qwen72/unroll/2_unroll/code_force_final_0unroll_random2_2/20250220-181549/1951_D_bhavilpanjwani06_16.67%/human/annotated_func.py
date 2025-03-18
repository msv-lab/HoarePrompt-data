#State of the program right berfore the function call: The function definition provided does not match the problem description. The correct function definition should be `def setup_store(t, test_cases):` where `t` is an integer representing the number of test cases (1 ≤ t ≤ 1000), and `test_cases` is a list of tuples, each containing two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively.
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
            #This is printed: n (where n is a positive integer between 1 and 10^18, and n is equal to k for the current test case)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: - The value of `n - k + 1` will be a positive integer because `n` is greater than or equal to `k`.
                #   - The value of `1` is a constant integer.
                #
                #Given the initial state and the conditions, the print statement will output the value of `n - k + 1` followed by `1`.
                #
                #Output:
            else :
                print('NO')
                #This is printed: NO
            #State: *`t` is an integer representing the number of test cases (1 ≤ t ≤ 1000), `test_cases` is a list of tuples, each containing two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), `n` is an input integer, `k` is an input integer, and `n` is greater than or equal to `k`. Additionally, `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, then the current value of `k - 1` is less than the current value of `n - k + 1`. Otherwise, `k - 1` is greater than or equal to `n - k + 1`.
        #State: *`t` is an integer representing the number of test cases (1 ≤ t ≤ 1000), `test_cases` is a list of tuples, each containing two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), `n` is an input integer, and `k` is an input integer. If `n` is equal to `k`, then `n` and `k` are the same. Otherwise, `n` is greater than `k`, and if `k - 1` is less than `n - k + 1`, then `k - 1` is less than `n - k + 1`. If `k - 1` is greater than or equal to `n - k + 1`, then `k - 1` is greater than or equal to `n - k + 1`.
    #State: *`t` is an integer representing the number of test cases (1 ≤ t ≤ 1000), `test_cases` is a list of tuples, each containing two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18), `n` is an input integer, and `k` is an input integer. If `n` is less than `k`, the current value of `n` is less than the current value of `k`. If `n` is equal to `k`, then `n` and `k` are the same. If `n` is greater than `k`, then `n` is greater than `k`, and the relationship between `k - 1` and `n - k + 1` is preserved: if `k - 1` is less than `n - k + 1`, then `k - 1` is less than `n - k + 1`; if `k - 1` is greater than or equal to `n - k + 1`, then `k - 1` is greater than or equal to `n - k + 1`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `n` represents the number of coins Alice has and `k` represents the number of jewels Bob wants Alice to buy. The function then checks if Alice can buy the jewels with her coins. If `n` is less than `k`, it prints "NO". If `n` is equal to `k`, it prints "YES", followed by "1" and the value of `n`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES", followed by "2" and the values `n - k + 1` and `1`. If `n` is greater than `k` and `k - 1` is greater than or equal to `n - k + 1`, it prints "NO". The function does not return any values; it only prints the results to the console.

