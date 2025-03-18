#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100, representing the number of cards and the number of cards exchanged in each operation, respectively. c is a list of n integers where 1 ≤ c_i ≤ 100, representing the numbers written on the cards.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        h = {}
        
        ans = n
        
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        
        print(ans)
        
    #State: _ is t-1, `t` is an integer such that 1 ≤ t ≤ 500, `n` is the first integer from the final input, `k` is the second integer from the final input, `a` is a list of integers from the final input, `h` is a dictionary where each key is an integer from `a` and its value is the count of occurrences of that integer in `a`. If any integer in `a` appears `k` or more times, `ams` is set to `k - 1`. Otherwise, `ams` remains undefined, and `ans` is equal to `n`.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves reading an integer `n` and another integer `k`, followed by a list of `n` integers `a`. The function counts the occurrences of each integer in `a` using a dictionary `h`. It then prints the value of `n` for each test case. The function does not return any values; instead, it prints the result directly. After processing all test cases, the final state includes the processed test cases and the printed results, but no modifications are made to the input variables.

