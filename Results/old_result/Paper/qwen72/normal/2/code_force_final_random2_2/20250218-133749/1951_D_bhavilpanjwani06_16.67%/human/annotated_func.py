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
            print(n)
            #This is printed: n (where n is a positive integer and n is equal to k, with 1 ≤ n, k ≤ 10^18)
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
            #State: t is an integer where 1 ≤ t ≤ 1000, n and k are positive integers where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively. Additionally, n is greater than or equal to k, and n is not equal to k. If \( k - 1 < n - k + 1 \), then the condition \( k - 1 < n - k + 1 \) holds true. Otherwise, \( k - 1 \geq n - k + 1 \).
        #State: t is an integer where 1 ≤ t ≤ 1000, n and k are positive integers where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively. Additionally, n is greater than or equal to k. If n == k, then n is exactly equal to k. Otherwise, n is greater than k, and either \( k - 1 < n - k + 1 \) or \( k - 1 \geq n - k + 1 \).
    #State: *t is an integer where 1 ≤ t ≤ 1000, n and k are positive integers where 1 ≤ n, k ≤ 10^18, representing the number of coins Alice has and the number of jewels Bob wants Alice to buy, respectively. If n < k, the current value of n is less than k. If n ≥ k, then either n is exactly equal to k, or n is greater than k, and the relationship between n and k can be either \( k - 1 < n - k + 1 \) or \( k - 1 \geq n - k + 1 \).
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `n` represents the number of coins Alice has and `k` represents the number of jewels Bob wants Alice to buy. The function checks if Alice can buy the required number of jewels based on the following conditions: If `n` is less than `k`, it prints "NO". If `n` is equal to `k`, it prints "YES", followed by "1" and the value of `n`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES", followed by "2" and the values `(n - k + 1, 1)`. Otherwise, it prints "NO". The function does not return any value; it only prints the results to the console. After the function concludes, the state of the program remains unchanged except for the output printed.

